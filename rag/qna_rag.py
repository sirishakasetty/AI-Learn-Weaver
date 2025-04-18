import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai
import os

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    """Ask OpenAI a question using the retrieved context."""
    context = "\n\n".join(retrieved_chunks)
    prompt = f"""
You are a helpful AI tutor. Based on the following context, answer the user's question.

--- CONTEXT ---
{context}

--- QUESTION ---
{question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You answer questions using only the given context. Be concise and clear."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response["choices"][0]["message"]["content"].strip()
