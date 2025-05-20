import logging
import os
from uuid import uuid4

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_pinecone import PineconeVectorStore
from openai import OpenAI
from pinecone import Pinecone

URL = "https://www.deeplearning.ai/the-batch/issue-{issue_number}/"

ISSUE_START = 290
ISSUE_LIMIT = 298

openai_client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_KEY", None),
)


async def scrape_weekly_issues(
    index, pinecone_client: Pinecone, logger: logging.Logger
) -> None:
    """Function to scrape the weekly issues of the deeplearning.ai website.

    Args:
        logger (logging.Logger, optional): Logger handler. Defaults to logger.
    """
    crawler_cfg = CrawlerRunConfig(
        exclude_external_links=True,
        exclude_social_media_links=True,  # skip Twitter, Facebook, etc.
        scan_full_page=True,  # scan the full page
        wait_for_images=True,  # ensure images are loaded
        verbose=True,
        page_timeout=1200000,
        log_console=True,
    )

    if not os.getenv("PINECONE_API_KEY"):
        raise ValueError("PINECONE_API_KEY environment variable not set.")

    async with AsyncWebCrawler(
        exclude_external_links=True,
        # exclude_social_media_links=True,
    ) as crawler:
        for issue in range(ISSUE_START, ISSUE_LIMIT + 1):
            # check if the issue already exists
            if os.path.exists(f"scrapped_issues/issue_{issue}.md"):
                logger.info("Issue %d already exists, skipping.", issue)
                continue

            # Use lazy % formatting in logging functions
            logger.info("Scraping issue %d", issue)
            result = await crawler.arun(
                url=URL.format(issue_number=issue),
                config=crawler_cfg,
            )

            if not result.success:
                logger.error("Failed to scrape issue %d", issue)
                raise Exception(f"Failed to scrape issue {issue}: {result.error}")

            with open(f"scrapped_issues/issue_{issue}.md", "w", encoding="utf-8") as f:
                f.write(result.markdown)

            # save_to_s3(
            #     s3_client,
            #     file_path=f"scrapped_issues/issue_{issue}.md",
            #     bucket_name="the-batch-markdown",
            #     object_name=f"scrapped_issues/issue_{issue}.md",
            # )
    save_to_pinecone(index=index, pinecone_client=pinecone_client)


def save_to_s3(s3_client, file_path, bucket_name, object_name):
    """Upload a file to an S3 bucket."""
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Successfully uploaded {file_path} to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")


def save_to_pinecone(index, pinecone_client: Pinecone):
    embeddings = NVIDIAEmbeddings(
        nvidia_api_key=os.environ.get("NVIDIA_KEY", ""), model="baai/bge-m3"
    )

    vector_store = PineconeVectorStore(index=index, embedding=embeddings)

    documents = []

    # open one by one files in a directory
    for issue in range(ISSUE_START, ISSUE_LIMIT + 1):
        markdown_path = f"scrapped_issues/issue_{issue}.md"
        loader = UnstructuredMarkdownLoader(
            file_path=markdown_path,
            mode="elements",
            strategy="hi_res",
        )
        loaded_document = loader.load()

        for document in loaded_document:
            if len(document.page_content) > 100:
                # add metadata to the document
                documents.append(document)

    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=uuids)
