import streamlit as st
import pickle
import pandas as pd
import requests

# -------------------- Helper Functions --------------------
def fetch_poster(movie_title):
    api_key = "ff780626"  # 🔑 Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        poster_url = data.get('Poster', '')
        # Handle missing or "N/A" poster values
        if not poster_url or poster_url == "N/A":
            return None
        return poster_url
    except requests.RequestException as e:
        print(f"Error fetching poster for {movie_title}: {e}")
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:13]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_posters

# -------------------- Load Pre-Processed Data --------------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# -------------------- Streamlit UI --------------------
st.title('🎬 Netflix-like Movie Recommendation System')

selected_movie_name = st.selectbox('Search for a movie to get recommendations:', movies['title'].values)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie_name)

    # Display posters in rows of 4
    num_cols = 4
    for row_idx in range(0, len(names), num_cols):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            if row_idx + col_idx < len(names):
                with cols[col_idx]:
                    if posters[row_idx + col_idx]:
                        st.image(posters[row_idx + col_idx], caption=names[row_idx + col_idx], use_container_width=True)
                    else:
                        st.write(f"🎥 {names[row_idx + col_idx]} (No poster available)")
