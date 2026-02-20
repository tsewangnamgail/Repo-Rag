github-repo-intelligence-rag/
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   │
│   │   ├── api/
│   │   │   ├── ingest.py
│   │   │   └── query.py
│   │   │
│   │   ├── core/
│   │   │   ├── rag_pipeline.py
│   │   │   ├── retriever.py
│   │   │   └── generator.py
│   │   │
│   │   ├── ingestion/
│   │   │   ├── clone_repo.py
│   │   │   ├── parser.py
│   │   │   └── chunker.py
│   │   │
│   │   ├── embeddings/
│   │   │   ├── embedder.py
│   │   │   └── vector_store.py
│   │   │
│   │   └── utils/
│   │       └── logger.py
│   │
│   ├── data/
│   │   ├── raw_repos/
│   │   └── vector_index/
│   │
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   │
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   │
│   │   ├── api/
│   │   │   └── client.js
│   │   │
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   ├── InputBox.jsx
│   │   │   └── RepoInput.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   ├── Dockerfile
│   └── .env
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md