from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.ingestion.clone_repo import clone_repository
from app.ingestion.parser import parse_repository
from app.ingestion.chunker import chunk_documents
from app.embeddings.vector_store import store_documents
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


class IngestRequest(BaseModel):
    repo_url: str


@router.post("/ingest")
async def ingest_repository(request: IngestRequest):
    try:
        repo_url = request.repo_url
        repo_name = repo_url.rstrip("/").split("/")[-1]

        logger.info(f"Starting ingestion for repo: {repo_url}")

        repo_path = clone_repository(repo_url)
        logger.info(f"Repository cloned at: {repo_path}")

        documents = parse_repository(repo_path)
        logger.info(f"Parsed {len(documents)} files")

        chunks = chunk_documents(documents)
        logger.info(f"Created {len(chunks)} chunks")

        store_documents(repo_name, chunks)
        logger.info(f"Stored embeddings in Chroma for repo: {repo_name}")

        return {
            "status": "success",
            "repo": repo_name,
            "files_parsed": len(documents),
            "chunks_indexed": len(chunks)
        }

    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))