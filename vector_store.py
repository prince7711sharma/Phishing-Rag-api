from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from knowledge_base import documents

model = SentenceTransformer("all-MiniLM-L6-v2")

# convert text → embeddings
embeddings = model.encode(documents)

# create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))


def search_similar(query, k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = [documents[i] for i in indices[0]]

    return results