import os
import time

import requests
from answer_relevancy import run_answer_relevancy
from deepeval.models import AmazonBedrockModel

model = AmazonBedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name="us-east-1",
    temperature=0.5,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)


def call_llm(input_text):
    """Call the LLM application and return the response."""
    response = requests.post(
        "http://127.0.0.1:8000/converse/",
        json={"query": input_text},
        timeout=30,
    )
    return response.json().get("response", {}).get("output", "")


USER_QUERY = "What are some news about Brain2Qwerty?"

EXPECTED_OUTPUT = """# Brain2Qwerty: Non-Invasive Brain-to-Text Translation\n\nBrain2Qwerty is a breakthrough non-invasive method that translates brain waves into text without requiring implanted electrodes. Here are the key details about this technology:\n\n- The system can accurately guess what a person is typing by reading their brain signals from outside the head\n- It uses either electroencephalogram (EEG) or magnetoencephalogram (MEG) technology to record brain activity\n- The research involved 35 healthy participants: 15 used EEG, 15 used MEG, and 5 used both devices\n- Participants were asked to read and memorize short Spanish-language sentences of 5-8 words\n- The research team included scientists from Meta, Paris Sciences et Lettres University, Hospital Foundation Adolphe de Rothschild, and several other institutions\n- Beyond just translating brain waves to text, the research also provided insights into how the brain processes language\n\n![Brain2Qwerty demonstration showing brain activity being decoded into text in real-time](https://dl-staging-website.ghost.io/content/images/2025/02/unnamed--50-.gif)\n\nThis technology represents significant progress in brain-computer interfaces that don't require surgical implantation of electrodes."""

llm_response = call_llm(USER_QUERY)

time.sleep(10)  # waiting to prevent throttling

results = []

answer_relevancy = run_answer_relevancy(
    user_input=USER_QUERY, actual_output=llm_response, model=model
)
results.append(answer_relevancy)

# TODO: connect to opensearch to get the retrieval context
# contextual_precision = run_contextual_precision()
# contextual_relevancy = run_contextual_relevancy()
# faithfulness = run_faithfulness()

print("Results:", results)
