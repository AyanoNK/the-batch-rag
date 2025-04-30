import logging
import os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig


URL = "https://www.deeplearning.ai/the-batch/issue-{issue_number}/"
ISSUE_NUMBER = 298


async def scrape_weekly_issues(s3_client, logger: logging.Logger) -> None:
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

    async with AsyncWebCrawler(
        exclude_external_links=True,
        # exclude_social_media_links=True,
    ) as crawler:
        for issue in range(1, ISSUE_NUMBER + 1):
            # Use lazy % formatting in logging functions
            logger.info("Scraping issue %d", issue)
            result = await crawler.arun(
                url=URL.format(issue_number=issue),
                config=crawler_cfg,
            )

            if not result.success:
                logger.error("Failed to scrape issue %d", issue)
                raise Exception(f"Failed to scrape issue {issue}: {result.error}")

            with open(f"issue_{issue}.md", "w", encoding="utf-8") as f:
                f.write(result.markdown)

            # save file in S3
            logger.info("Uploading issue %d to S3", issue)
            s3_client.upload_file(
                Filename=f"issue_{issue}.md",
                Bucket="the-batch-markdown",
                Key=f"issue_{issue}.md",
            )

            # remove file
            logger.info("Removing issue %d file", issue)
            os.remove(f"issue_{issue}.md")
