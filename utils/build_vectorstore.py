import os
import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS_FOLDER = os.path.join(BASE_DIR, "Docs")
VECTOR_DB = os.path.join(BASE_DIR, "VectorStore")

os.makedirs(VECTOR_DB, exist_ok=True)

chunks = []

CHUNK_SIZE = 500
OVERLAP = 100

for file in os.listdir(DOCS_FOLDER):

    if file.endswith(".md"):

        path = os.path.join(DOCS_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "source": file
            })

            start += CHUNK_SIZE - OVERLAP

print(f"Created {len(chunks)} chunks")

texts = [c["text"] for c in chunks]

embeddings = model.encode(
    texts,
    convert_to_numpy=True,
    show_progress_bar=True
)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype("float32"))

faiss.write_index(
    index,
    os.path.join(VECTOR_DB, "index.faiss")
)

with open(
    os.path.join(VECTOR_DB, "documents.pkl"),
    "wb"
) as f:
    pickle.dump(chunks, f)

print("Vector Store Created Successfully!")