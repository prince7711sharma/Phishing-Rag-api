from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from knowledge_base import documents

model = None
index = None


def load_store():
    global model, index

    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = model.encode(documents)

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings))


def search_similar(query, k=3):
    load_store()

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = [documents[i] for i in indices[0]]
    return results