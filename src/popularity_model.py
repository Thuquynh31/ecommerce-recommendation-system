# ==============================
# POPULARITY-BASED RECOMMENDER
# ==============================

def get_popular_products(
    df,
    top_n=10
):

    popular_products = (

        df
        .sort_values(
            by=["rating", "root_bs_rank"],
            ascending=[False, True]
        )

    )

    return popular_products[
        [
            "title",
            "brand",
            "rating",
            "department"
        ]
    ].head(top_n)


# ==============================
# POPULARITY EVALUATION
# ==============================

def evaluate_popularity(
    df,
    top_n=10
):

    popular_products = get_popular_products(
        df,
        top_n
    )

    avg_rating = (
        popular_products["rating"]
        .mean()
    )

    print("=" * 50)
    print(
        "POPULARITY-BASED EVALUATION"
    )
    print("=" * 50)

    print(
        f"Average Rating@{top_n}: {avg_rating:.2f}"
    )

    return popular_products