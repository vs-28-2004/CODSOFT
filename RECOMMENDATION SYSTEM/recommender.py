def calculate_genre_match(selected_genres, genres):
    selected_set = set(selected_genres.split("|"))
    movie_set = set(genres.split("|"))

    if "(no genres listed)" in movie_set:
        return 0

    matching_genres = selected_set.intersection(movie_set)
    return len(matching_genres)


def recommend_movies(movie_title, movie_data, num_recommendations):
    selected_movie = movie_data[
        movie_data["title"] == movie_title
    ].iloc[0]

    selected_genres = selected_movie["genres"]

    recommendations = movie_data[
        movie_data["title"] != movie_title
    ].copy()

    recommendations["genre_match"] = recommendations["genres"].apply(
        lambda genre: calculate_genre_match(
            selected_genres,
            genre,
        )
    )

    recommendations = recommendations[
        (recommendations["genre_match"] > 0)
        & (recommendations["rating_count"] >= 20)
    ]

    recommendations["final_score"] = (
        recommendations["genre_match"] * 2
        + recommendations["average_rating"]
        + recommendations["rating_count"] / 1000
    )

    recommendations = recommendations.sort_values(
        by=["final_score", "average_rating", "rating_count"],
        ascending=False,
    )

    return recommendations.head(num_recommendations)