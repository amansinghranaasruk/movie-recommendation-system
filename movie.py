import streamlit as st
import random

movies = {
    "Action": ["John Wick", "Avengers", "Mad Max"],
    "Comedy": ["3 Idiots", "Free Guy", "The Hangover"],
    "Sci-Fi": ["Interstellar", "The Matrix", "Inception"]
}

st.title("🎬 Movie Recommendation System")

genre = st.selectbox("Choose a genre", list(movies.keys()))

if st.button("Recommend"):
    st.success(random.choice(movies[genre]))
