from app.embeddings.vector_store import get_vector_store


def get_retriever(repo_name: str):
    vector_store = get_vector_store(repo_name)

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5}
    )

    return retriever