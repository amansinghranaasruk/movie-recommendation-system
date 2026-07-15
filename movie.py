import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

movies = pd.read_csv("movies.csv")

# ---------------- TITLE ---------------- #

st.title("🎬 Movie Recommendation System")

st.markdown(
    "Find your next favorite movie based on **Language, Genre, Year and IMDb Rating**."
)

# ---------------- DASHBOARD ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎬 Movies", len(movies))

with col2:
    st.metric("🎭 Genres", movies["Genre"].nunique())

with col3:
    st.metric("🌍 Languages", movies["Language"].nunique())

st.divider()

# ---------------- SEARCH ---------------- #

search = st.text_input("🔍 Search Movie")

if search:
    result = movies[
        movies["Movie"].str.contains(search, case=False, na=False)
    ]

    if result.empty:
        st.warning("Movie not found.")
    else:
        st.dataframe(result)

st.divider()

# ---------------- FILTERS ---------------- #

language = st.selectbox(
    "🌍 Choose Language",
    sorted(movies["Language"].unique())
)

genre = st.selectbox(
    "🎭 Choose Genre",
    sorted(movies["Genre"].unique())
)

start_year, end_year = st.slider(
    "📅 Release Year",
    int(movies["Year"].min()),
    int(movies["Year"].max()),
    (2000, 2025)
)

num_movies = st.slider(
    "🎬 Number of Recommendations",
    1,
    10,
    5
)

sort_option = st.selectbox(
    "📊 Sort By",
    ["Highest Rated", "Newest", "Random"]
)

st.divider()

# ---------------- SURPRISE ME ---------------- #

if st.button("🎲 Surprise Me"):
    random_movie = movies.sample(1).iloc[0]

    st.success(f"🎬 {random_movie['Movie']}")

    st.write(f"⭐ IMDb Rating: {random_movie['IMDb_Rating']}")
    st.write(f"📅 Year: {random_movie['Year']}")
    st.write(f"🎭 Genre: {random_movie['Genre']}")
    st.write(f"🌍 Language: {random_movie['Language']}")

st.divider()

# ---------------- RECOMMEND BUTTON ---------------- #

if st.button("🎥 Recommend Movies"):

    filtered = movies[
        (movies["Language"] == language)
        &
        (movies["Genre"] == genre)
        &
        (movies["Year"] >= start_year)
        &
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

        st.success("Recommended Movies")

        for _, row in recommendations.iterrows():

            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(
                    "https://placehold.co/250x350?text=Movie+Poster",
                    width=180
                )

            with col2:

                st.subheader(f"🎬 {row['Movie']}")

                st.write(f"⭐ IMDb Rating : {row['IMDb_Rating']}")

                st.write(f"📅 Release Year : {row['Year']}")

                st.write(f"🎭 Genre : {row['Genre']}")

                st.write(f"🌍 Language : {row['Language']}")

                st.divider()
