# The Batch RAG Backend

This is the backend for The Batch RAG, a website tailored to put weekly news about AI.

The Batch RAG is a project that aims to create a Retrieval-Augmented Generation (RAG) system using the latest news articles from The Batch. The project involves scraping data from The Batch, storing it in a vector database, and implementing a query system for retrieval.

## Requirements

- Have an AWS account
- Have set up the necessary AWS services, including S3, Bedrock, IAM, and OpenSearch Serverless.
- Have run the Scrapper script to scrape the data from The Batch and store it in S3.
- Have created the necessary resources in AWS, including the OpenSearch Serverless collection and the Bedrock knowledge base.
- Python 3.8 or higher
- Installed dependencies from `requirements.txt`

## Installation

First, install the required dependencies to run the project.

```bash
pip install -r requirements.txt
```

Make sure that you are logged in to your AWS account using the AWS CLI with SSO or equivalent AWS environment variables.

Finally, run the following command to start the server

```bash
python main.py
```

## Configuration

- `main.py` contains the configuration for the script.
