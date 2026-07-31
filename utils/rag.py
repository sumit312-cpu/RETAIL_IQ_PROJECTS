import os

os.environ["USE_TF"] = "0"
os.environ["USE_TORCH"] = "1"

import pickle
import faiss

from sentence_transformers import SentenceTransformer


class RAGRetriever:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        VECTOR_DB = os.path.join(
            BASE_DIR,
            "VectorStore"
        )

        self.index = faiss.read_index(
            os.path.join(VECTOR_DB, "index.faiss")
        )

        with open(
            os.path.join(VECTOR_DB, "documents.pkl"),
            "rb"
        ) as f:

            self.documents = pickle.load(f)

    def retrieve(self, query, top_k=4):

        embedding = self.model.encode([query])

        _, indices = self.index.search(
            embedding.astype("float32"),
            top_k
        )

        context = ""

        sources = set()

        for idx in indices[0]:

            context += self.documents[idx]["text"] + "\n\n"

            sources.add(
                self.documents[idx]["source"]
            )

        return context, list(sources)