from langchain_core.language_models import BaseChatModel
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_pinecone import PineconeVectorStore

PROMPT = """
You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.

Question: {query}
Context: {context}
Answer:
"""

prompt_template = ChatPromptTemplate(
    [
        ("system", PROMPT),
    ]
)


def query_response(
    query: str, vector_store: PineconeVectorStore, nvidia_llm: BaseChatModel
) -> str:
    """Query the vector store and get a response from the LLM.

    Args:
        query (str): The query string that the human user has asked.
        vector_store (PineconeVectorStore): The vector store to search for relevant documents.
        nvidia_llm (BaseChatModel): The LLM to generate the response.

    Returns:
        str: The generated response from the LLM.
    """
    retrieved_docs = vector_store.similarity_search(query, k=5)
    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
    example_messages = prompt_template.invoke({"context": docs_content, "query": query})

    answer = nvidia_llm.invoke(example_messages)
    return answer.content
