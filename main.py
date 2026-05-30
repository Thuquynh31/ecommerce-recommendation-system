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


# ==============================
# LOAD DATA
# ==============================

df = pd.read_csv(
    "data/amazon_products.csv"
)

# ==============================
# PREPROCESSING
# ==============================

df = clean_data(df)

# ==============================
# FEATURE ENGINEERING
# ==============================

df = create_combined_features(df)

tfidf_matrix, cosine_sim = (
    create_similarity_matrix(df)
)
# ==============================
# POPULAR PRODUCTS
# ==============================

print("\nPOPULAR PRODUCTS\n")

print(
    get_popular_products(df)
)

# ==============================
# CONTENT-BASED RECOMMENDATION
# ==============================

print("\nRECOMMENDED PRODUCTS\n")

print(

    recommend_products(
        "iPhone",
        df,
        cosine_sim
    )

)