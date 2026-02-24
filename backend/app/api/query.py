from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.rag_pipeline import run_rag
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


class QueryRequest(BaseModel):
    question: str
    repo_name: str


@router.post("/query")
async def query_repository(request: QueryRequest):
    try:
        logger.info(f"Query received for repo: {request.repo_name}")

        answer = run_rag(
            repo_name=request.repo_name,
            question=request.question
        )

        logger.info("Query processed successfully")

        return {
            "status": "success",
            "answer": answer
        }

    except Exception as e:
        logger.error(f"Query failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))