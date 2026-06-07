import streamlit as st

from components import (
    show_dataset_stats,
    show_header,
    show_recommendations,
    show_selected_movie,
)
from config import APP_TITLE, APP_SUBTITLE, DATASET_PATH
from data_loader import load_data
from recommender import recommend_movies
from styles import apply_styles


st.set_page_config(page_title=APP_TITLE, layout="wide")

apply_styles()

try:
    # Load dataset
    movies, ratings, movie_df = load_data(DATASET_PATH)

    # Header section
    show_header(APP_TITLE, APP_SUBTITLE)
    show_dataset_stats(movies, ratings)

    st.divider()

    col1, col2 = st.columns([1, 2])

    # Left side
    with col1:
        st.subheader("Choose Movie")

        movie_list = movie_df.sort_values("title")["title"].tolist()
        selected_movie = st.selectbox(
            "Select a movie you like",
            movie_list,
        )

        total_recommendations = st.slider(
            "Number of recommendations",
            min_value=5,
            max_value=15,
            value=10,
        )

        movie_info = movie_df[movie_df["title"] == selected_movie].iloc[0]
        show_selected_movie(movie_info)

    # Right side
    with col2:
        st.subheader("Movies You May Like")

        recommended_movies = recommend_movies(
            selected_movie,
            movie_df,
            total_recommendations,
        )

        show_recommendations(recommended_movies)

    st.divider()

    with st.expander("View sample dataset"):
        st.dataframe(movie_df.head(30), use_container_width=True)

except FileNotFoundError:
    st.error(
        "Dataset files were not found. Please check the DATASET_PATH in config.py."
    )

except Exception as e:
    st.error(f"Error: {e}")