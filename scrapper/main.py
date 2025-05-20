import asyncio
import logging
import os
import sys

from pinecone import Pinecone, ServerlessSpec

from scrappers.weekly_issues import scrape_weekly_issues

LOG_NAME = "weekly_issues.log"
LOG_FORMAT = "%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s"

# session = Session(
#     region_name="us-east-1",
#     profile_name="bedrock",
# )

# s3_client = session.client(
#     "s3",
# )

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(
    api_key=pinecone_api_key,
)


logging.basicConfig(
    filename=LOG_NAME,
    filemode="a",
    format=LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


INDEX_NAME = "the-batch-index"

if not pc.has_index(INDEX_NAME):
    pc.create_index(
        name=INDEX_NAME,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(INDEX_NAME)

logger = logging.getLogger("weekly_issues")
logger.addHandler(logging.StreamHandler(sys.stdout))


if __name__ == "__main__":
    asyncio.run(scrape_weekly_issues(index=index, pinecone_client=pc, logger=logger))
