import os
from langchain_community.vectorstores import Chroma
from app.config import settings
from app.embeddings.embedder import get_embedding_model


def get_vector_store(repo_name: str):
    persist_directory = os.path.join(
        settings.CHROMA_PERSIST_DIRECTORY,
        repo_name
    )

    embedding_model = get_embedding_model()

    return Chroma(
        collection_name=repo_name,
        embedding_function=embedding_model,
        persist_directory=persist_directory
    )


def store_documents(repo_name: str, documents):
    vector_store = get_vector_store(repo_name)

    texts = [doc["content"] for doc in documents]
    metadatas = [doc["metadata"] for doc in documents]

    vector_store.add_texts(texts=texts, metadatas=metadatas)
    vector_store.persist()

    return vector_store