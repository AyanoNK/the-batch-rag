# the-batch-rag

See the results at [https://the-batch-rag.onrender.com/](https://the-batch-rag.onrender.com/)

The Batch is a weekly newsletter by Andrew Ng that covers the latest developments in AI and machine learning. It is a great resource for anyone interested in staying up-to-date with the latest trends and advancements in the field.
This project is a simple web application that allows users to search for specific topics in the newsletter and get relevant information. The application uses a combination of web scraping, natural language processing, and machine learning to provide accurate and relevant results.

## Approach

Andrew's Letters, Data Points, ML Research, Business, Science, Culture, Hardware, and AI Careers categories are just rewrites of the Weekly Issues. Therefore, one can only scrape the Weekly Issues and not the other categories.

### Usage

See the official documentation and approach [here](DOCS.md).

### Setup

1. Set up the scrapper and scrape the data from The Batch. Follow instructions in the [scrapper](scrapper/README.md) folder.
2. Set up the vector database and embeddings. Follow instructions in the [cloud documentation using AWS](CLOUD.md).
3. Set up the backend API. Follow instructions in the [backend](backend/README.md) folder.
4. Set up the frontend. Follow instructions in the [frontend](frontend/README.md) folder.

## Roadmap

### Setting the project up

- [x] Create and deploy the frontend base app
- [x] Create and deploy a base backend API

### Setting up the project environemnt

- [x] Create the chat frontend
- [x] Create the backend API with some mock calls for the frontend to call
- [x] Create the vector database for embeddings

### Scrapping

- [x] Create a scrapper to get the data from The Batch

### Interaction

- [x] Use an LLM to interact with the user, using the vector database to retrieve data from the user query
- [x] Use the LLM to generate a summary of the data retrieved from the vector database.
- [x] Use the resulting summary to expose an API endpoint.

## Reference

- https://learn.deeplearning.ai/courses/advanced-retrieval-for-ai/lesson/ukzj4/overview-of-embeddings-based-retrieval
- https://learn.deeplearning.ai/courses/building-evaluating-advanced-rag/lesson/e8xng/advanced-rag-pipeline
- https://learn.deeplearning.ai/courses/function-calling-and-data-extraction-with-llms/lesson/pxion/function-calling-variations
- https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/uymu6/tracing-agents
- https://huggingface.co/spaces/hesamation/primer-llm-embedding?section=tf-idf_%28term_frequency-inverse_document_frequency%29
- https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf

### Embedding models

- https://huggingface.co/spaces/mteb/leaderboard
- https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/
- https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-embedding
- https://docs.anthropic.com/en/docs/build-with-claude/embeddings

### Scrapping

- https://github.com/lavague-ai/LaVague
- https://github.com/ScrapeGraphAI/Scrapegraph-ai

### Testing

- https://www.deepeval.com/docs/getting-started

### Observability

- https://arize.com/

### DevOps

- https://bun.sh/guides/ecosystem/render
- https://www.youtube.com/watch?v=0Xyn8HD2abU

### Frontend tricks

- https://chrome.dev/
