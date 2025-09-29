
import pickle
import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide", page_title="🍿 Movie Recommender")

# ================== Dark Theme CSS ==================
st.markdown(
    """
    <style>
    body {
        background-color: #141414;
        color: white;
    }
    .stApp {
        background-color: #141414;
        color: white;
    }
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    img {
        transition: transform 0.3s ease;
        border-radius: 15px;
    }
    img:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 20px rgba(255,0,0,0.7);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================== TMDB API ==================
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_movie_details(movie_id):
    """Fetch movie details from TMDB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster = "https://image.tmdb.org/t/p/w500/" + data.get('poster_path') if data.get('poster_path') else "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"
    overview = data.get('overview', 'No description available.')
    tmdb_url = f"https://www.themoviedb.org/movie/{movie_id}"
    return poster, overview, tmdb_url

def fetch_watch_providers(movie_id, region="US"):
    """Fetch streaming providers with TMDB watch page link."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={API_KEY}"
    data = requests.get(url).json()
    region_data = data.get("results", {}).get(region, {})
    providers = region_data.get("flatrate", [])
    watch_link = region_data.get("link", None)  # TMDB watch page for this movie

    provider_list = []
    for p in providers:
        provider_list.append((p["provider_name"], watch_link))

    if not provider_list:
        provider_list = [("Not available for streaming in your region", None)]

    return provider_list

# ================== Recommender ==================
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("❌ Movie not found in the dataset.")
        return []
    
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        year = movies.iloc[i[0]].year
        rating = movies.iloc[i[0]].vote_average
        poster, overview, tmdb_url = fetch_movie_details(movie_id)
        providers = fetch_watch_providers(movie_id)
        recommendations.append((title, poster, year, rating, overview, tmdb_url, providers))
    return recommendations

# ================== Load Data ==================
try:
    movies_dict = pickle.load(open('artifacts/movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("⚠️ Model files not found. Please run the data processing notebook first.")
    st.stop()

# ================== UI ==================
st.title("🎬 Movie Recommender System")
st.caption("Find your next binge-worthy movie 🍿 — with streaming info included!")

movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Select a movie you like:", movie_list)

if st.button("🔍 Show Recommendations"):
    with st.spinner("🍿 Grabbing some popcorn and finding movies..."):
        recommendations = recommend(selected_movie)

    if recommendations:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                title, poster, year, rating, overview, tmdb_url, providers = recommendations[i]

                # Poster with link
                st.markdown(
                    f"<a href='{tmdb_url}' target='_blank'><img src='{poster}'></a>",
                    unsafe_allow_html=True
                )

                # Movie Info
                st.markdown(f"**{title}**")
                st.caption(f"📅 {int(year) if pd.notna(year) else 'N/A'}")
                stars = "⭐" * int(round(rating/2))
                st.caption(f"{stars} ({rating:.1f}/10)")
                st.markdown(f"<small>{overview[:100]}...</small>", unsafe_allow_html=True)

                # Streaming Availability (Clickable)
                st.markdown("**📺 Available On:**")
                for p_name, link in providers:
                    if link:
                        st.markdown(f"- [✅ {p_name}]({link})", unsafe_allow_html=True)
                    else:
                        st.caption(f"❌ {p_name}")