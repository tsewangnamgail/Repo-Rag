from langchain_core.prompts import ChatPromptTemplate
from app.core.retriever import get_retriever
from app.core.generator import get_llm


def run_rag(repo_name: str, question: str):
    retriever = get_retriever(repo_name)
    llm = get_llm()

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = ChatPromptTemplate.from_template(
        """
You are a senior software engineer.

Use the following repository context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and explain the code if needed.
"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content