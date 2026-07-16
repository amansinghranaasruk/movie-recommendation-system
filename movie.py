import streamlit as st
import pandas as pd

# ---------------- PAGE ----------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(rgba(8,8,8,.90),rgba(8,8,8,.92)),
url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1800&q=80");
background-size:cover;
background-attachment:fixed;
color:white;
}

h1{
text-align:center;
font-size:60px;
color:white;
}

.big{
text-align:center;
font-size:22px;
color:#dddddd;
margin-bottom:25px;
}

[data-testid="metric-container"]{
background:#151515;
border-radius:15px;
padding:20px;
border:1px solid #333;
}

.stButton>button{
background:#E50914;
color:white;
font-size:20px;
font-weight:bold;
width:100%;
height:55px;
border:none;
border-radius:10px;
}

.stButton>button:hover{
background:#ff3030;
}

.movie{
background:#1b1b1b;
padding:20px;
border-radius:15px;
margin-bottom:15px;
border-left:5px solid red;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------

movies = pd.read_csv("movies.csv")

# ---------------- TITLE ----------------

st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

st.markdown(
"<p class='big'>Find your next favourite movie from 500+ movies.</p>",
unsafe_allow_html=True)

# ---------------- METRICS ----------------

c1,c2,c3,c4=st.columns(4)

c1.metric("🎞 Movies",len(movies))
c2.metric("🎭 Genres",movies["Genre"].nunique())
c3.metric("🌍 Languages",movies["Language"].nunique())
c4.metric("⭐ Avg IMDb",round(movies["IMDb"].mean(),1))

st.divider()

# ---------------- SEARCH ----------------

search=st.text_input("🔍 Search Movie")

if search:

    result=movies[movies["Movie"].str.contains(search,case=False)]

    if len(result):

        st.success(f"{len(result)} movie found")

        st.dataframe(result,use_container_width=True)

st.divider()

# ---------------- FILTERS ----------------

col1,col2,col3=st.columns(3)

with col1:
    language=st.selectbox(
        "Language",
        sorted(movies["Language"].unique())
    )

with col2:
    genre=st.selectbox(
        "Genre",
        sorted(movies["Genre"].unique())
    )

with col3:
    rating=st.slider(
        "Minimum IMDb",
        0.0,
        10.0,
        7.0,
        0.1
    )

year=st.slider(
    "Release Year",
    int(movies["Year"].min()),
    int(movies["Year"].max()),
    (
        int(movies["Year"].min()),
        int(movies["Year"].max())
    )
)

count=st.slider(
    "Number of Recommendations",
    1,
    20,
    10
)

# ---------------- BUTTON ----------------

if st.button("🍿 Recommend Movies"):

    result=movies[
        (movies["Language"]==language)&
        (movies["Genre"]==genre)&
        (movies["IMDb"]>=rating)&
        (movies["Year"]>=year[0])&
        (movies["Year"]<=year[1])
    ]

    if len(result)==0:

        st.warning("No movies found.")

    else:

        st.subheader("🎬 Recommended Movies")

        for _,row in result.head(count).iterrows():

            st.markdown(f"""
<div class="movie">

## 🎥 {row['Movie']}

⭐ IMDb : **{row['IMDb']}**

🎭 Genre : **{row['Genre']}**

🌍 Language : **{row['Language']}**

📅 Year : **{row['Year']}**

</div>
""",unsafe_allow_html=True)
#101820
))
color:white;
}

/* Hide Streamlit Menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Hero Banner */

.hero{
padding:45px;
border-radius:25px;
background:
linear-gradient(
90deg,
rgba(229,9,20,.95),
rgba(20,20,20,.85)
);

box-shadow:0px 15px 35px rgba(0,0,0,.5);
margin-bottom:30px;
animation:fadeIn 1s;
}

.hero h1{
font-size:58px;
font-weight:700;
margin-bottom:10px;
color:white;
}

.hero p{
font-size:22px;
color:#f1f1f1;
}

/* Statistics */

.metric-card{

background:rgba(255,255,255,.08);

backdrop-filter:blur(12px);

padding:25px;

border-radius:20px;

text-align:center;

transition:.4s;

border:1px solid rgba(255,255,255,.15);

box-shadow:0px 8px 25px rgba(0,0,0,.4);

}

.metric-card:hover{

transform:translateY(-8px);

background:rgba(255,255,255,.12);

}

/* Search */

.stTextInput input{

background:#202020;

border-radius:12px;

border:1px solid #444;

color:white;

}

/* Selectbox */

div[data-baseweb="select"]{

background:#202020;

border-radius:12px;

}

/* Sliders */

.stSlider{

padding-top:15px;

}

/* Buttons */

.stButton>button{

background:#E50914;

color:white;

border:none;

padding:14px;

border-radius:12px;

font-size:18px;

font-weight:bold;

transition:.4s;

width:100%;

}

.stButton>button:hover{

background:#ff3030;

transform:scale(1.03);

}

/* Movie Card */

.movie-card{

background:#1d1d1d;

padding:25px;

border-radius:18px;

margin-bottom:18px;

box-shadow:0px 8px 25px rgba(0,0,0,.4);

border-left:8px solid #E50914;

transition:.4s;

}

.movie-card:hover{

transform:translateY(-6px);

}

.rating{

color:#FFD700;

font-weight:bold;

font-size:20px;

}

@keyframes fadeIn{

from{opacity:0;transform:translateY(20px);}
to{opacity:1;transform:translateY(0px);}

}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero ---------------- #

st.markdown(st.markdown("""
<style>

/* ---------- Background ---------- */
.stApp{
background:
radial-gradient(circle at top left,#3b0a45 0%,transparent 35%),
radial-gradient(circle at top right,#0b4f6c 0%,transparent 35%),
radial-gradient(circle at bottom,#111827 20%,#000000 90%);
background-attachment:fixed;
color:white;
}

/* Hide Streamlit header */
header{visibility:hidden;}

/* Main container */
.block-container{
padding-top:2rem;
padding-bottom:2rem;
max-width:1200px;
}

/* Title */
h1{
text-align:center;
font-size:56px !important;
font-weight:900 !important;
color:white;
letter-spacing:1px;
text-shadow:0px 0px 25px rgba(255,0,100,.6);
}

/* Subtitle */
.subtitle{
text-align:center;
font-size:20px;
color:#dddddd;
margin-bottom:35px;
}

/* Metric Cards */

[data-testid="metric-container"]{
background:rgba(255,255,255,.08);
backdrop-filter:blur(18px);
border-radius:20px;
padding:20px;
border:1px solid rgba(255,255,255,.1);
box-shadow:0px 10px 35px rgba(0,0,0,.45);
transition:.3s;
}

[data-testid="metric-container"]:hover{
transform:translateY(-6px);
box-shadow:0px 15px 45px rgba(255,0,100,.35);
}

/* Input Boxes */

.stSelectbox div[data-baseweb="select"]>div,
.stTextInput input{
background:rgba(255,255,255,.08);
border-radius:15px;
border:1px solid rgba(255,255,255,.15);
}

/* Slider */

.stSlider>div>div>div>div{
background:#ff1744;
}

/* Button */

.stButton>button{
width:100%;
height:60px;
border-radius:18px;
font-size:22px;
font-weight:bold;
background:linear-gradient(90deg,#ff1744,#ff9100);
color:white;
border:none;
transition:.35s;
box-shadow:0px 8px 25px rgba(255,0,80,.45);
}

.stButton>button:hover{
transform:scale(1.04);
background:linear-gradient(90deg,#ff4081,#ffc107);
box-shadow:0px 15px 40px rgba(255,0,80,.6);
}

/* Movie Cards */

.movie-card{
background:rgba(255,255,255,.08);
backdrop-filter:blur(15px);
padding:22px;
border-radius:18px;
margin-bottom:18px;
border-left:6px solid #ff1744;
box-shadow:0px 10px 35px rgba(0,0,0,.45);
transition:.3s;
}

.movie-card:hover{
transform:translateY(-6px);
box-shadow:0px 15px 45px rgba(255,0,100,.45);
}

/* Scrollbar */

::-webkit-scrollbar{
width:10px;
}

::-webkit-scrollbar-thumb{
background:#ff1744;
border-radius:20px;
}

::-webkit-scrollbar-track{
background:#111;
}

</style>
""", unsafe_allow_html=True))

# ---------------- Stats ---------------- #

c1,c2,c3=st.columns(3)

with c1:
    st.markdown(f"""
    <div class='metric-card'>
    <h2>🎬</h2>
    <h1>{len(movies)}</h1>
    <p>Total Movies</p>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='metric-card'>
    <h2>🎭</h2>
    <h1>{movies['Genre'].nunique()}</h1>
    <p>Genres</p>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='metric-card'>
    <h2>🌍</h2>
    <h1>{movies['Language'].nunique()}</h1>
    <p>Languages</p>
    </div>
    """,unsafe_allow_html=True)

st.write("")
st.write("")
