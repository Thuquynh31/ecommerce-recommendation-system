import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


# ==============================
# COMBINE FEATURES
# ==============================

def create_combined_features(df):

    df["combined_features"] = (

        df["title"].fillna('') + " " +

        df["brand"].fillna('') + " " +

        df["description"].fillna('') + " " +

        df["categories"].fillna('') + " " +

        df["department"].fillna('')

    )

    # Remove rows with very little information
    df = df[
        df["combined_features"]
        .str.len() > 20
    ]

    # Reset index
    df = df.reset_index(
        drop=True
    )

    return df


# ==============================
# TF-IDF + COSINE SIMILARITY
# ==============================

def create_similarity_matrix(df):

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = tfidf.fit_transform(
        df["combined_features"]
    )

    cosine_sim = cosine_similarity(
        tfidf_matrix
    )

    return tfidf_matrix, cosine_sim


# ==============================
# CREATE INDICES
# ==============================

def create_indices(df):

    indices = pd.Series(
        df.index,
        index=df["title"]
    ).drop_duplicates()

    return indices