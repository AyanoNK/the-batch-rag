"""Base FastAPI application with a couple of endpoints."""

from typing import TypeVar

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

from config import Settings
from llm_client import BedrockClient

T = TypeVar("T")
context: dict[str, T] = {}


class UserQuery(BaseModel):
    """Model for user query."""

    query: str = Field(min_length=5, default="What are some news about Brain2Qwerty?")


def get_bedrock_client() -> BedrockClient:
    """Dependency to get BedrockClient instance."""
    return BedrockClient()


async def lifespan(_: FastAPI):
    """Lifespan event to initialize and clean up resources."""
    ## Initialize resources here
    # env vars
    context["env"] = Settings()
    aws_bedrock_flow_id = context["env"].aws_bedrock_flow_id
    aws_access_key_id = context["env"].aws_access_key_id
    aws_secret_access_key = context["env"].aws_secret_access_key

    # bedrock client
    bedrock_client = BedrockClient(
        aws_bedrock_flow_id=aws_bedrock_flow_id,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    context["bedrock_client"] = bedrock_client
    yield
    # Clean up resources here
    context["bedrock_client"].client.close()


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://the-batch-rag.onrender.com/",
    "the-batch-rag.onrender.com/",
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
    """Converse with the LLM using the BedrockClient.
    This endpoint takes a user query and generates a response using the
    BedrockClient.

    Args:
        user_query (UserQuery): The user query to be processed.

    Returns:
        dict: _description_
    """
    bedrock_client: BedrockClient = context["bedrock_client"]
    generated_response = bedrock_client.generate_response(
        query=user_query.query,
    )

    return {
        "response": generated_response,
    }


if __name__ == "__main__":
    uvicorn.run(app)
