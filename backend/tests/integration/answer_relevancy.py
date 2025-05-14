from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import DeepEvalBaseLLM
from deepeval.test_case import LLMTestCase

# Answer Relevancy Metric


def run_answer_relevancy(
    user_input, actual_output: str, model: DeepEvalBaseLLM
) -> None:
    metric = AnswerRelevancyMetric(threshold=0.7, model=model, include_reason=True)
    test_case = LLMTestCase(
        input=user_input,
        actual_output=actual_output,
    )

    evaluation_result = evaluate(test_cases=[test_case], metrics=[metric])
    return evaluation_result
