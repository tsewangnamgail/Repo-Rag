import os
import shutil
import subprocess
from app.config import settings


def clone_repository(repo_url: str) -> str:
    repo_name = repo_url.rstrip("/").split("/")[-1]
    repo_path = os.path.join(settings.REPO_STORAGE_PATH, repo_name)

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    os.makedirs(settings.REPO_STORAGE_PATH, exist_ok=True)

    subprocess.run(
        ["git", "clone", repo_url, repo_path],
        check=True
    )

    return repo_path