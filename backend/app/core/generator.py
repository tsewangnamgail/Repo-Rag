from langchain_groq import ChatGroq
from app.config import settings


def get_llm():
    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name="llama3-70b-8192",
        temperature=0.2
    )