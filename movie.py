import streamlit as st
import pandas as pd

# -------------------------
# Page Settings
# -------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
movies = pd.read_csv("movies.csv")

# -------------------------
# Title
# -------------------------
st.title("🎬 Movie Recommendation System")
st.write("Find your next favorite movie!")

st.divider()

# -------------------------
# Statistics
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🎥 Movies", len(movies))
col2.metric("🎭 Genres", movies["Genre"].nunique())
col3.metric("🌍 Languages", movies["Language"].nunique())

st.divider()

# -------------------------
# Search
# -------------------------
search = st.text_input("🔍 Search Movie")

if search:
    result = movies[movies["Movie"].str.contains(search, case=False)]

    if len(result) > 0:
        st.dataframe(result, use_container_width=True)
    else:
        st.warning("Movie not found.")

st.divider()

# -------------------------
# Filters
# -------------------------
language = st.selectbox(
    "Select Language",
    sorted(movies["Language"].unique())
)

genre = st.selectbox(
    "Select Genre",
    sorted(movies["Genre"].unique())
)

year = st.slider(
    "Select Release Year",
    int(movies["Year"].min()),
    int(movies["Year"].max()),
    int(movies["Year"].min())
)

rating = st.slider(
    "Minimum IMDb Rating",
    0.0,
    10.0,
    7.0,
    0.1
)

count = st.slider(
    "Number of Recommendations",
    1,
    20,
    10
)

# -------------------------
# Recommend Button
# -------------------------
if st.button("🍿 Recommend Movies"):

    recommendations = movies[
        (movies["Language"] == language) &
        (movies["Genre"] == genre) &
        (movies["Year"] >= year) &
        (movies["IMDb"] >= rating)
    ]

    if recommendations.empty:
        st.warning("No movies found.")
    else:
        st.success(f"Found {len(recommendations)} movies")

        for _, row in recommendations.head(count).iterrows():

            st.markdown("---")

            st.subheader(row["Movie"])

            st.write(f"⭐ IMDb : {row['IMDb']}")
            st.write(f"🎭 Genre : {row['Genre']}")
            st.write(f"🌍 Language : {row['Language']}")
            st.write(f"📅 Year : {row['Year']}")
