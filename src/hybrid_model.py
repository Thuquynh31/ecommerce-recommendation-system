from src.popularity_model import (
    get_popular_products
)

from src.content_based_model import (
    recommend_products
)


# ==============================
# HYBRID RECOMMENDATION SYSTEM
# ==============================

def hybrid_recommendation(

    user_type,

    df,

    cosine_sim=None,

    keyword=None,

    top_n=10
):

    # ==============================
    # NEW USERS
    # ==============================

    if user_type == "new":

        print("=" * 50)

        print(
            "POPULAR PRODUCTS "
            "FOR NEW USERS"
        )

        print("=" * 50)

        return get_popular_products(
            df,
            top_n
        )

    # ==============================
    # SEARCH USERS
    # ==============================

    elif user_type == "search":

        print("=" * 50)

        print(
            "CONTENT-BASED "
            "RECOMMENDATIONS"
        )

        print("=" * 50)

        return recommend_products(

            keyword,

            df,

            cosine_sim,

            top_n
        )

    # ==============================
    # EXISTING USERS
    # ==============================

    elif user_type == "existing":

        print("=" * 50)

        print(
            "COLLABORATIVE FILTERING "
            "RECOMMENDATIONS"
        )

        print("=" * 50)

        return (
            "Recommendations "
            "based on user similarity."
        )

    # ==============================
    # INVALID INPUT
    # ==============================

    else:

        return "Invalid user type."