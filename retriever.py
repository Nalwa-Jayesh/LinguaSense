import os
import numpy as np
import faiss
from langdetect import detect
from sentence_transformers import SentenceTransformer
from transformers import pipeline

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class Retriever:
    def __init__(self, doc_folder="documents", chunk_size=200):
        self.texts = []
        self.langs = []
        self.embeddings = []
        self.index = faiss.IndexFlatL2(384)
        self._load_documents(doc_folder, chunk_size)

    def _chunk_text(self, text, chunk_size):
        words = text.split()
        return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def _load_documents(self, path, chunk_size):
        for fname in os.listdir(path):
            with open(os.path.join(path, fname), "r", encoding="utf-8") as f:
                full_text = f.read()
                chunks = self._chunk_text(full_text, chunk_size)
                for chunk in chunks:
                    lang = detect(chunk)
                    self.texts.append(chunk)
                    self.langs.append(lang)
                    self.embeddings.append(model.encode(chunk))
        self.index.add(np.array(self.embeddings, dtype=np.float32))

    def query(self, query_text, k=3):
        query_vec = model.encode(query_text).reshape(1, -1).astype(np.float32)
        _, indices = self.index.search(query_vec, k)
        return [self.texts[i] for i in indices[0]]

    def get_concise_answer(self, query_text, k=3, max_summary_length=150):
        retrieved_texts = self.query(query_text, k)
        combined_text = " ".join(retrieved_texts)
        summary = summarizer(combined_text, max_length=max_summary_length, min_length=30, do_sample=False)
        return summary[0]['summary_text']
