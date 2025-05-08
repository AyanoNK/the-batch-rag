"""Common module to encapsulate LLM, and implementation of Amazon Bedrock."""

import logging
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass

import boto3
from botocore import config as boto_config

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LLMClient(ABC):
    """An abstract class to encapsulate stateless interaction with LLM"""

    def __init__(self, *args, **kwargs):
        """Abstract constructor"""

    @abstractmethod
    def generate_response(self, query, *args, **kwargs):
        """An abstract method"""
        raise NotImplementedError()


@dataclass
class Boto3SessionConfig:
    """Configuration for Boto3 session."""

    region_name: str = "us-east-1"
    profile_name: str = "bedrock"
    dict = asdict


class BedrockClient(LLMClient):
    """Implementation of _LLMClient for Amazon Bedrock."""

    def __init__(self, *, aws_bedrock_flow_id: str = None, **kwargs):
        """Constructor.

        Even though the interation with Bedrock is stateless, this class
        maintains an instance of boto3 client object in it.

        Args:
            config: An instance of BedrockConfig.
                If None, default values will be used.
        """
        if not aws_bedrock_flow_id:
            raise ValueError("aws_bedrock_flow_id is required")

        self._config = Boto3SessionConfig()

        session_kwargs = self._config.dict()

        # validate if AWS keys are in kwargs
        if "aws_access_key_id" in kwargs and "aws_secret_access_key" in kwargs:
            session_kwargs["aws_access_key_id"] = kwargs.get(
                "aws_access_key_id", "MOCK_ACCESS_KEY_ID"
            )
            session_kwargs["aws_secret_access_key"] = kwargs.get(
                "aws_secret_access_key", "MOCK_SECRET_ACCESS_KEY"
            )

        self._session = boto3.Session(**session_kwargs)

        self.bedrock_agent = self._session.client(
            service_name="bedrock-agent",
            config=boto_config.Config(
                retries={
                    "max_attempts": 10,
                    "mode": "standard",
                },
            ),
        )

        self.bedrock_flow = self.bedrock_agent.get_flow(
            flowIdentifier=aws_bedrock_flow_id
        )
        print("FOUND FLOW WITH ID: ", self.bedrock_flow.get("id"))

        self.bedrock_runtime_client = self._session.client("bedrock-agent-runtime")

    def generate_response(self, query: str, *args, **kwargs):
        response = self.bedrock_runtime_client.invoke_flow(
            enableTrace=True,
            flowAliasIdentifier="IHPCFM5D0T",
            flowIdentifier=self.bedrock_flow.get("id"),
            inputs=[
                {
                    "content": {"document": query},
                    "nodeName": "FlowInputNode",
                    "nodeOutputName": "document",
                },
            ],
            modelPerformanceConfiguration={
                "performanceConfig": {"latency": "standard"}
            },
        )

        flow_status = ""
        output = ""

        for event in response["responseStream"]:
            # Check if flow is complete.
            if "flowCompletionEvent" in event:
                flow_status = event["flowCompletionEvent"]["completionReason"]

            # Save the model output.
            elif "flowOutputEvent" in event:
                output = event["flowOutputEvent"]["content"]["document"]

            # Log trace events.
        return {"flow_status": flow_status, "output": output}
