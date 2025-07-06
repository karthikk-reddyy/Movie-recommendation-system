import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# ------------------ Load movies.pkl ------------------
with open('movies.pkl', 'rb') as f:
    movies = pickle.load(f)

# ------------------ Handle Missing Values ------------------
# If genres are missing, fill with empty string
movies['genres'] = movies['genres'].fillna('')

# ------------------ TF-IDF Vectorization ------------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# ------------------ Calculate Cosine Similarity ------------------
similarity = cosine_similarity(tfidf_matrix)

# ------------------ Save Similarity Matrix ------------------
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("✅ similarity.pkl generated successfully!")
