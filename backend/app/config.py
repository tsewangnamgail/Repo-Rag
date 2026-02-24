from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GROQ_API_KEY: str
    CHROMA_PERSIST_DIRECTORY: str = "data/vector_index"
    REPO_STORAGE_PATH: str = "data/raw_repos"

    class Config:
        env_file = ".env"


settings = Settings()