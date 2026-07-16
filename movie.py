import streamlit as st
import pandas as pd
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

/* Main title */
h1{
text-align:center;
color:white;
font-size:52px;
}

/* Subtitle */
p{
font-size:18px;
}

/* Metric Cards */
[data-testid="metric-container"]{
background:rgba(255,255,255,0.08);
border-radius:18px;
padding:18px;
border:1px solid rgba(255,255,255,.2);
box-shadow:0px 5px 20px rgba(0,0,0,.4);
}

/* Buttons */
.stButton>button{
background:#E50914;
color:white;
border:none;
border-radius:10px;
height:55px;
width:100%;
font-size:18px;
font-weight:bold;
}

.stButton>button:hover{
background:#ff1f1f;
}

/* Select boxes */
div[data-baseweb="select"]{
background:#1F2937;
border-radius:10px;
}

/* Text Input */
.stTextInput input{
background:#1F2937;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

movies = pd.read_csv("movies.csv")

# ---------------- TITLE ----------------

st.title("🎬 Movie Recommendation System")

st.markdown(
"""
Find your next favorite movie based on **language, genre, release year and IMDb rating.**
"""
)

st.divider()

# ---------------- STATS ----------------

col1, col2, col3 = st.columns(3)

col1.metric("🎬 Total Movies", len(movies))
col2.metric("🎭 Genres", movies["Genre"].nunique())
col3.metric("🌍 Languages", movies["Language"].nunique())

st.divider()

# ---------------- SEARCH ----------------

search = st.text_input("🔍 Search Movie")

if search:

    result = movies[
        movies["Movie"].str.contains(search, case=False, na=False)
    ]

    if len(result):

        st.subheader("Search Results")

        st.dataframe(
            result[
                ["Movie","Genre","Language","Year","IMDb_Rating"]
            ],
            use_container_width=True
        )

    else:
        st.warning("Movie not found.")

st.divider()

# ---------------- FILTERS ----------------

language = st.selectbox(
    "🌍 Select Language",
    sorted(movies["Language"].unique())
)

genre = st.selectbox(
    "🎭 Select Genre",
    sorted(movies["Genre"].unique())
)

year_range = st.slider(
    "📅 Select Release Year",
    int(movies["Year"].min()),
    int(movies["Year"].max()),
    (
        int(movies["Year"].min()),
        int(movies["Year"].max())
    )
)

rating = st.slider(
    "⭐ Minimum IMDb Rating",
    0.0,
    10.0,
    7.0,
    0.1
)

recommendations = st.slider(
    "🎥 Number of Recommendations",
    1,
    20,
    10
)

st.write("")

# ---------------- BUTTON ----------------

if st.button("🍿 Recommend Movies"):

    filtered = movies[

        (movies["Language"] == language)

        &

        (movies["Genre"] == genre)

        &

        (movies["Year"] >= year_range[0])

        &

        (movies["Year"] <= year_range[1])

        &

        (movies["IMDb_Rating"] >= rating)

    ]

    if len(filtered)==0:

        st.error("❌ No movies found. Try changing filters.")

    else:

        if len(filtered) > recommendations:

            filtered = filtered.sample(recommendations)

        st.success(f"Found {len(filtered)} movie(s)")

        st.write("")

        for _, row in filtered.iterrows():

            st.markdown(f"""
### 🎬 {row['Movie']}

**🎭 Genre:** {row['Genre']}

**🌍 Language:** {row['Language']}

**📅 Year:** {row['Year']}

**⭐ IMDb:** {row['IMDb_Rating']}

---
""")

st.divider()

st.caption("Made with ❤️ using Python, Pandas and Streamlit")

