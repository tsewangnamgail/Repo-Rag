from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ingest, query

app = FastAPI(
    title="GitHub Repo Intelligence RAG",
    description="Chat with any GitHub repository using Groq + RAG",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, prefix="/api")
app.include_router(query.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}