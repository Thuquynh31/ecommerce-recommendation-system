# ==============================
# CONTENT-BASED RECOMMENDER
# ==============================

def recommend_products(
    keyword,
    df,
    cosine_sim,
    top_n=10
):

    # Search matching products
    matches = df[
        df["title"]
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

    # No match found
    if matches.empty:

        return (
            "No matching products found."
        )

    # First matched product
    matched_product = matches.iloc[0]

    # Product index
    idx = matched_product.name

    # Similarity scores
    sim_scores = list(
        enumerate(cosine_sim[idx])
    )

    # Sort similarity
    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Top recommendations
    sim_scores = sim_scores[
        1:top_n+1
    ]

    # Product indices
    product_indices = [

        i[0]
        for i in sim_scores

    ]

    print("=" * 50)
    print(
        "SEARCH KEYWORD:",
        keyword
    )

    print("MATCHED PRODUCT:")

    print(
        matched_product["title"]
    )

    print("=" * 50)

    return df[
        [
            "title",
            "brand",
            "department",
            "rating"
        ]
    ].iloc[product_indices]


# ==============================
# CONTENT-BASED EVALUATION
# ==============================

def precision_at_k(
    keyword,
    df,
    cosine_sim,
    k=10
):

    # Find matching product
    matches = df[
        df["title"]
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

    if matches.empty:

        return (
            "No matching product found."
        )

    # Query product
    query_product = matches.iloc[0]

    query_department = (
        query_product["department"]
    )

    # Recommendations
    recommendations = recommend_products(
        keyword,
        df,
        cosine_sim,
        top_n=k
    )

    # Relevant recommendations
    relevant = recommendations[
        recommendations["department"]
        == query_department
    ]

    # Precision@K
    precision = len(relevant) / k

    print("=" * 50)
    print(
        "CONTENT-BASED EVALUATION"
    )
    print("=" * 50)

    print(
        f"Precision@{k}: {precision:.2f}"
    )

    return recommendations