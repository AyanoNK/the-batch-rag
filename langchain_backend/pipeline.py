from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_pinecone import PineconeVectorStore

PROMPT = """
You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Context: {context}
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", PROMPT),
        ("human", "{input}"),
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

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    question_answer_chain = create_stuff_documents_chain(nvidia_llm, prompt_template)
    chain = create_retrieval_chain(
        retriever=retriever, combine_docs_chain=question_answer_chain
    )

    answer = chain.invoke({"input": query})

    source_files = set([doc.metadata.get("filename", "") for doc in answer["context"]])

    return {
        "answer": answer.get("answer"),
        "source_documents": source_files,
    }
