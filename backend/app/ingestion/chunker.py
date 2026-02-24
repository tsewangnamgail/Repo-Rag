from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = []

    for doc in documents:
        split_texts = splitter.split_text(doc["content"])

        for chunk in split_texts:
            chunks.append({
                "content": chunk,
                "metadata": doc["metadata"]
            })

    return chunks