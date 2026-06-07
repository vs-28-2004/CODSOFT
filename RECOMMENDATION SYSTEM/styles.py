import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
            .main-title {
                font-size: 38px;
                font-weight: 700;
                margin-bottom: 4px;
                color: white;
            }

            .subtitle {
                color: #5f6b7a;
                font-size: 17px;
                margin-bottom: 24px;
            }

            .movie-card {
                border: 1px solid #dde3ea;
                border-radius: 8px;
                padding: 14px 16px;
                margin-bottom: 10px;
                background: #ffffff;
                color: #111827;
            }

            .movie-title {
                font-size: 17px;
                font-weight: 700;
                color: #111827;
            }

            .movie-meta {
                color: #475467;
                font-size: 14px;
                margin-top: 4px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
