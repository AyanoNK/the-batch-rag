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

## Usage

### Spinning up the server

The server is built using FastAPI and runs on port 8000 by default. You can change the port by modifying the `port` variable in `main.py`.

This server is also built using Boto3 to create a new Bedrock client to interact with the Bedrock service.
That said, [llm_client.py](llm_client.py) contains a generic class to have not only the configuration for the Bedrock client, but other future implementations.

### Routes

There are two routes available in the backend:

- `/`: This route will redirect GET requests to the documentation OpenAPI service.
- `/converse`: This is the main route of the application. It is used to communicate with Python backend service. It returns a JSON response with the answer to the question asked by the user. Keep in mind that the response will be in Markdown format.

  - The request body should contain a JSON object with the following structure:

  ```json
  {
    "query": "What is the latest news about AI?"
  }
  ```

  - The response will be a JSON object with the following structure:

  ```json
  {
    "answer": "The latest news about AI is...",
    "response": {
      "flow_status": "The status of the Bedrock Flow's executiion",
      "output": "The output of the Bedrock Flow in Markdown format"
    }
  }
  ```
