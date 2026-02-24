import os

ALLOWED_EXTENSIONS = {".py", ".js", ".ts", ".md", ".txt"}


def parse_repository(repo_path: str):
    documents = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            ext = os.path.splitext(file)[1]

            if ext in ALLOWED_EXTENSIONS:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    documents.append({
                        "content": content,
                        "metadata": {
                            "file_name": file,
                            "file_path": file_path
                        }
                    })

                except Exception:
                    continue

    return documents