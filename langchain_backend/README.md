# The Batch RAG Backend

This is the backend for The Batch RAG, a website tailored to put weekly news about AI.

The Batch RAG is a project that aims to create a Retrieval-Augmented Generation (RAG) system using the latest news articles from The Batch. The project involves scraping data from The Batch, storing it in a vector database, and implementing a query system for retrieval.

## Requirements

- Have a Pinecone account
- Have an NVIDIA account
- Installed dependencies from `requirements.txt`

## Installation

First, install the required dependencies to run the project.

```bash
pip install -r requirements.txt
```

Then, create a `.env` file in the root directory of the project following the `.env.example`

Finally, run the following command to start the server

```bash
python main.py
```

## Configuration

- `main.py` contains the configuration for the script.

## Usage

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
    "source_documents": [
      "A list of the documents queried to your vector database",
      "to generate an answer"
    ]
  }
  ```
