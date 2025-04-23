# the-batch-rag

https://www.deeplearning.ai/the-batch/

## TODO

### Setting the project up

- [x] Create and deploy the frontend base app
- [ ] Create and deploy a base backend API

### Setting up the project environemnt

- [ ] Create the chat frontend
- [ ] Create the backend API with some mock calls for the frontend to call
- [ ] Create the vector database for embeddings

### Scrapping

- [ ] Create a scrapper to get the data from The Batch
- [ ] Expose the scrapper as an interface

### Embedding

- [ ] Create a cronjob that takes the data from the scrapper and embeds it
- [ ] Use the cronjob to upload the embeddings to the vector database. Beware of duplicates.

### Interaction

- [ ] Use an LLM to interact with the user, using the vector database to retrieve data from the user query
- [ ] Use the LLM to generate a summary of the data retrieved from the vector database.
- [ ] Use the resulting summary to expose an API endpoint.

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
