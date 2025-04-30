import asyncio
import logging
import sys
from boto3 import Session

from scrappers.weekly_issues import scrape_weekly_issues

LOG_NAME = "weekly_issues.log"
LOG_FORMAT = "%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s"

session = Session(
    region_name="us-east-1",
    profile_name="bedrock",
)

s3_client = session.client(
    "s3",
)


logging.basicConfig(
    filename=LOG_NAME,
    filemode="a",
    format=LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger("weekly_issues")
logger.addHandler(logging.StreamHandler(sys.stdout))


if __name__ == "__main__":
    asyncio.run(scrape_weekly_issues(s3_client, logger))
