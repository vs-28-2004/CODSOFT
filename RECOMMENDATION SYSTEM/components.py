import html
import streamlit as st


def show_header(title, subtitle):
    st.markdown(
        f'<div class="main-title">{html.escape(title)}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="subtitle">{html.escape(subtitle)}</div>',
        unsafe_allow_html=True,
    )


def show_dataset_stats(movie_data, rating_data):
    total_movies = len(movie_data)
    total_ratings = len(rating_data)
    total_users = rating_data["userId"].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Movies", total_movies)
    col2.metric("Total Ratings", total_ratings)
    col3.metric("Total Users", total_users)


def show_selected_movie(movie_details):
    st.info(
        f"Selected movie: {movie_details['title']}\n\n"
        f"Genres: {movie_details['genres']}\n\n"
        f"Average rating: {movie_details['average_rating']:.2f}"
    )


def show_movie_card(movie, rank):
    title = html.escape(str(movie["title"]))
    genres = html.escape(str(movie["genres"]).replace("|", ", "))

    st.markdown(
        f"""
        <div class="movie-card">
            <div class="movie-title">{rank}. {title}</div>
            <div class="movie-meta">{genres}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_recommendations(recommended_movies):
    if len(recommended_movies) == 0:
        st.warning("No recommendations found for this movie.")
        return

    for rank, (_, movie) in enumerate(
        recommended_movies.iterrows(),
        start=1,
    ):
        show_movie_card(movie, rank)