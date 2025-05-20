"""Base FastAPI application with a couple of endpoints."""

from typing import TypeVar

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from langchain.chat_models import init_chat_model
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from pydantic import BaseModel, Field

from config import Settings
from llm_client import NVIDIAOpenAIClient
from pipeline import query_response

T = TypeVar("T")

INDEX_NAME = "the-batch-index"
context: dict[str, T] = {}


class UserQuery(BaseModel):
    """Model for user query."""

    query: str = Field(min_length=5, default="What are some news about Brain2Qwerty?")


def get_nvidia_client(nvidia_key: str) -> NVIDIAOpenAIClient:
    """Dependency to get NVIDIAOpenAIClient instance."""
    return NVIDIAOpenAIClient(
        NVIDIA_KEY=nvidia_key,
    )


async def lifespan(_: FastAPI):
    """Lifespan event to initialize and clean up resources."""
    ## Initialize resources here
    context["env"] = Settings()
    context["nvidia_client"] = get_nvidia_client(context["env"].nvidia_key)
    context["nvidia_chat_llm"] = init_chat_model(
        "meta/llama3-70b-instruct",
        model_provider="nvidia",
        nvidia_api_key=context["env"].nvidia_key,
    )

    # NVIDIA embeddings
    embeddings = NVIDIAEmbeddings(
        nvidia_api_key=context["env"].nvidia_key, model="baai/bge-m3"
    )

    # pinecone

    pc = Pinecone(
        api_key=context["env"].pinecone_api_key,
    )

    index = pc.Index(INDEX_NAME)
    context["vector_store"] = PineconeVectorStore(embedding=embeddings, index=index)

    yield
    # Clean up resources here


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "https://the-batch-rag.onrender.com",
    "https://the-batch-rag.onrender.com:10000",
    "the-batch-rag.onrender.com",
    "the-batch-rag.onrender.com:10000",
]


app = FastAPI(debug=True, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    """Redirect to the documentation page."""
    return RedirectResponse("/docs", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/converse/")
def converse(user_query: UserQuery) -> dict:
    """Converse with the LLM using the NVIDIAOpenAIClient.
    This endpoint takes a user query and generates a response using the
    NVIDIAOpenAIClient.

    Args:
        user_query (UserQuery): The user query to be processed.

    Returns:
        dict: _description_
    """
    llm_response = query_response(
        query=user_query.query,
        vector_store=context["vector_store"],
        nvidia_llm=context["nvidia_chat_llm"],
    )

    return {
        "response": llm_response,
    }


if __name__ == "__main__":
    uvicorn.run(app)
