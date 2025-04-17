import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import subprocess

# Load embedding model once
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=300):
    """Split text into chunks of N words."""
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def embed_chunks(chunks):
    """Embed chunks using a sentence transformer model."""
    embeddings = embedding_model.encode(chunks)
    return np.array(embeddings).astype("float32")

def build_faiss_index(chunks):
    """Create a FAISS index from text chunks."""
    index = faiss.IndexFlatL2(embedding_model.get_sentence_embedding_dimension())
    embeddings = embed_chunks(chunks)
    index.add(embeddings)
    return index, embeddings, chunks

def retrieve_context(question, index, chunks, embeddings, top_k=3):
    """Retrieve top-k relevant chunks from FAISS index for a question."""
    q_embed = embedding_model.encode([question]).astype("float32")
    distances, indices = index.search(q_embed, top_k)
    return [chunks[i] for i in indices[0]]

def ask_question(question, retrieved_chunks):
    """Ask Gemma a question using retrieved context."""
    prompt = f"""
You are an educational AI assistant. Use the following context to answer the student's question clearly.

--- Context ---
{''.join(retrieved_chunks)}

--- Question ---
{question}
"""

    result = subprocess.run(
        ["ollama", "run", "gemma:7b", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",   # Fix for UnicodeDecodeError
        errors="ignore"     # Graceful fallback
    )

    return result.stdout.strip()
