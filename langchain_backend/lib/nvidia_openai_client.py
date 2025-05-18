"""Common module to encapsulate LLM, and implementation of Amazon Bedrock."""

import logging
from openai import OpenAI
from llm_client import LLMClient


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



class NVIDIAOpenAIClient(LLMClient):
    """Implementation of _LLMClient for NVIDIA."""

    def __init__(self, *args, **kwargs):
        client = OpenAI(
            base_url = "https://integrate.api.nvidia.com/v1",
            api_key = kwargs.get("NVIDIA_KEY", None),
        )
        self.client = client


    def generate_response(self, query: str, *args, **kwargs):
        
        """Generate response from NVIDIA LLM."""
