import pandas as pd
import streamlit as st


@st.cache_data
def load_data(data_path):
    movies_df = pd.read_csv(f"{data_path}/movies.csv")
    ratings_df = pd.read_csv(f"{data_path}/ratings.csv")

    rating_stats = (
        ratings_df.groupby("movieId")
        .agg(
            average_rating=("rating", "mean"),
            rating_count=("rating", "count"),
        )
        .reset_index()
    )

    combined_data = movies_df.merge(
        rating_stats,
        on="movieId",
        how="left",
    )

    combined_data["average_rating"] = (
        combined_data["average_rating"].fillna(0)
    )

    combined_data["rating_count"] = (
        combined_data["rating_count"]
        .fillna(0)
        .astype(int)
    )

    return movies_df, ratings_df, combined_data