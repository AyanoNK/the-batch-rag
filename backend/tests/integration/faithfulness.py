from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase


def test_faithfulness(user_input, actual_output, retrieval_context: list, model):
    """
    Run the Faithfulness metric on the given test case.

    Args:
        user_input (str): The input query from the user.
        actual_output (str): The actual output from the LLM.
        retrieval_context (list): The context retrieved by the RAG pipeline.
        model: The model used for evaluation.

    Returns:
        None
    """
    metric = FaithfulnessMetric(threshold=0.7, model=model, include_reason=True)
    test_case = LLMTestCase(
        input=user_input,
        actual_output=actual_output,
        retrieval_context=retrieval_context,
    )

    evaluate(test_cases=[test_case], metrics=[metric])
