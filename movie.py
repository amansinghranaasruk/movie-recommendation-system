import streamlit as st
import pandas as pd
import random

# Load dataset
movies = pd.read_csv("movies.csv")

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

st.markdown(
    "Find your next favorite movie based on genre, language, and release year."
)

# 👇 ADD THIS HERE
col1, col2, col3 = st.columns(3)

col1.metric("Movies", len(movies))
col2.metric("Genres", movies["Genre"].nunique())
col3.metric("Languages", movies["Language"].nunique())

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
sort_option = st.selectbox(
    "Sort By",
    ["Highest Rated", "Newest", "Random"]
)

if st.button("🎬 Recommend Movies"):

    filtered = movies[
        (movies["Language"] == language) &
        (movies["Genre"] == genre) &
        (movies["Year"] >= start_year) &
        (movies["Year"] <= end_year)
    ]

    if filtered.empty:
        st.warning("No movies found.")
    else:

        if sort_option == "Highest Rated":
            recommendations = filtered.sort_values(
                by="IMDb_Rating",
                ascending=False
            ).head(num_movies)

        elif sort_option == "Newest":
            recommendations = filtered.sort_values(
                by="Year",
                ascending=False
            ).head(num_movies)

        else:
            recommendations = filtered.sample(
                min(num_movies, len(filtered))
            )

        for _, row in recommendations.iterrows():

    with st.container():

        st.markdown(
        f"""
        <div style="
            border:2px solid #444;
            border-radius:15px;
            padding:20px;
            margin-bottom:20px;
            background-color:#1f1f1f;
        ">

        <h2>🎬 {row['Movie']}</h2>

        ⭐ <b>IMDb Rating:</b> {row['IMDb_Rating']}<br>

        📅 <b>Release Year:</b> {row['Year']}<br>

        🎭 <b>Genre:</b> {row['Genre']}<br>

        🌍 <b>Language:</b> {row['Language']}

        </div>
        """,
        unsafe_allow_html=True
        )
