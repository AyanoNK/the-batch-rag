"""Common module to encapsulate LLM, and implementation of Amazon Bedrock."""

from abc import ABC, abstractmethod

from openai import OpenAI


class LLMClient(ABC):
    """An abstract class to encapsulate stateless interaction with LLM"""

    def __init__(self, *args, **kwargs):
        """Abstract constructor"""

    @abstractmethod
    def generate_response(self, query, *args, **kwargs):
        """An abstract method"""
        raise NotImplementedError()


class NVIDIAClient(LLMClient):
    """Implementation of _LLMClient for NVIDIA."""

    def __init__(self, *args, **kwargs):
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=kwargs.get("NVIDIA_KEY", None),
        )
        self.client: OpenAI = client

    def generate_response(self, query: str, *args, **kwargs):
        """Generate response from NVIDIA LLM."""

        completion = self.client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-ultra-253b-v1",
            messages=[
                {"role": "system", "content": "detailed thinking on"},
                {"role": "user", "content": "What is the definition of insanity?"},
            ],
            temperature=0.6,
            top_p=0.95,
            max_tokens=4096,
            frequency_penalty=0,
            presence_penalty=0,
            stream=True,
        )

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
