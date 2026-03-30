from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_documents(file_path):
    docs = []
    with open(file_path, 'r') as f:
        for line in f:
            doc_id, text = line.strip().split("|")
            docs.append(text)
    return docs

documents = load_documents("documents.txt")

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def rank_documents(query):
    query_vector = vectorizer.transform([query])
    similarity = cosine_similarity(query_vector, doc_vectors)
    ranked_indices = np.argsort(similarity[0])[::-1]
    
    results = []
    for idx in ranked_indices:
        results.append({
            "document": documents[idx],
            "score": float(similarity[0][idx])
        })
    return results






