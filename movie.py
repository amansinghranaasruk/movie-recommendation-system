import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

try:
    movies = pd.read_csv("movies.csv")
except FileNotFoundError:
    st.error("movies.csv not found!")
    st.stop()

# ---------------- TITLE ---------------- #

st.title("🎬 Movie Recommendation System")

st.write(
    "Find your next favorite movie based on language, genre, year and IMDb rating."
)

st.divider()

# ---------------- DASHBOARD ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎬 Total Movies", len(movies))

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
    "🌍 Select Language",
    sorted(movies["Language"].unique())
)

genre = st.selectbox(
    "🎭 Select Genre",
    sorted(movies["Genre"].unique())
)

start_year, end_year = st.slider(
    "📅 Select Release Year",
    int(movies["Year"].min()),
    int(movies["Year"].max()),
    (
        int(movies["Year"].min()),
        int(movies["Year"].max())
    )
)

num_movies = st.slider(
    "🎬 Number of Recommendations",
    1,
    10,
    5
)

sort_option = st.selectbox(
    "📊 Sort By",
    [
        "Highest Rated",
        "Newest",
        "Random"
    ]
)

st.divider()

# ---------------- SURPRISE ME ---------------- #

if st.button("🎲 Surprise Me"):

    movie = movies.sample(1).iloc[0]

    st.success("Here's a random movie for you!")

    st.subheader(movie["Movie"])

    st.write(f"⭐ IMDb Rating: {movie['IMDb_Rating']}")
    st.write(f"📅 Year: {movie['Year']}")
    st.write(f"🎭 Genre: {movie['Genre']}")
    st.write(f"🌍 Language: {movie['Language']}")

st.divider()

# ---------------- RECOMMEND ---------------- #

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

        st.warning("❌ No movies found. Try changing the filters.")

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

        st.success(f"Found {len(recommendations)} movie(s)!")

        for _, row in recommendations.iterrows():

            with st.container():

                st.subheader(f"🎬 {row['Movie']}")

                c1, c2 = st.columns(2)

                with c1:
                    st.write(f"⭐ **IMDb Rating:** {row['IMDb_Rating']}")
                    st.write(f"📅 **Release Year:** {row['Year']}")

                with c2:
                    st.write(f"🎭 **Genre:** {row['Genre']}")
                    st.write(f"🌍 **Language:** {row['Language']}")

                st.divider()
