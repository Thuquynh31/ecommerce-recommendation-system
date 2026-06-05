import streamlit as st
import pandas as pd

from src.preprocessing import clean_data

from src.feature_engineering import (
    create_combined_features,
    create_similarity_matrix
)

from src.content_based_model import (
    recommend_products
)

from src.popularity_model import (
    get_popular_products
)

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/amazon_products.csv",
        encoding="ISO-8859-1"
    )

    df = clean_data(df)

    df = create_combined_features(df)

    _, cosine_sim = (
        create_similarity_matrix(df)
    )

    return df, cosine_sim


df, cosine_sim = load_data()

# =========================
# STREAMLIT UI
# =========================

st.title(
    "E-Commerce Recommendation System"
)

st.write(
    "Product recommendation using "
    "Content-Based Filtering"
)

# =========================
# USER INPUT
# =========================

keyword = st.text_input(
    "Enter product keyword:"
)

# =========================
# BUTTON
# =========================

if st.button("Recommend Products"):

    if keyword:

        recommendations = recommend_products(
            keyword,
            df,
            cosine_sim
        )

        st.write(
            "Recommended Products:"
        )

        st.dataframe(
            recommendations
        )

    else:

        st.warning(
            "Please enter a keyword."
        )

# =========================
# POPULAR PRODUCTS
# =========================

st.subheader(
    "Popular Products"
)

popular_products = (
    get_popular_products(df)
)

st.dataframe(
    popular_products
)