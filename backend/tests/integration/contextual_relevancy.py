# Contextual Relevancy Metric
from deepeval import evaluate
from deepeval.metrics import ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase


def run_contextual_relevancy(
    expected_output, actual_output, retrieval_context, model
) -> None:
    """
    Run the Contextual Relevancy metric on the given test case.

    Args:
        expected_output (str): The expected output from the LLM.
        actual_output (str): The actual output from the LLM.
        retrieval_context (list): The context retrieved by the RAG pipeline.

    Returns:
        None
    """
    metric = ContextualRelevancyMetric(threshold=0.7, model=model, include_reason=True)
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output=actual_output,
        expected_output=expected_output,
        retrieval_context=retrieval_context,
    )

    evaluate(test_cases=[test_case], metrics=[metric])
