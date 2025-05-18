"""Common module to encapsulate LLM, and implementation of Amazon Bedrock."""

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass

class LLMClient(ABC):
    """An abstract class to encapsulate stateless interaction with LLM"""

    def __init__(self, *args, **kwargs):
        """Abstract constructor"""

    @abstractmethod
    def generate_response(self, query, *args, **kwargs):
        """An abstract method"""
        raise NotImplementedError()

