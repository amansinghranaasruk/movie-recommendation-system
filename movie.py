import streamlit as st
import pandas as pd
import random

# Load dataset
movies = pd.read_csv("movies.csv")

st.title("🎬 Movie Recommendation System")

# Language
language = st.selectbox(
    "Choose Language",
    sorted(movies["Language"].unique())
)

# Genre
genre = st.selectbox(
    "Choose Genre",
    sorted(movies["Genre"].unique())
)

# Year
start_year, end_year = st.slider(
    "Choose Release Year",
    1950,
    2025,
    (1990, 2025)
)

# Number of movies
num_movies = st.slider(
    "Number of Recommendations",
    1,
    10,
    5
)

# Filter movies
filtered = movies[
    (movies["Language"] == language) &
    (movies["Genre"] == genre) &
    (movies["Year"] >= start_year) &
    (movies["Year"] <= end_year)
]

# Recommend button
if st.button("🎥 Recommend Movies"):

    if filtered.empty:
        st.warning("No movies found.")
    else:
        recommendations = filtered.sample(
            min(num_movies, len(filtered))
        )

        st.success("Recommended Movies")

        for _, row in recommendations.iterrows():
            st.write(f"🎬 **{row['Movie']}** ({row['Year']})")
