import pandas as pd


# ==============================
# FIX ENCODING
# ==============================

def fix_encoding(text):

    try:

        return (
            text
            .encode("latin1")
            .decode("utf-8")
        )

    except Exception:

        return text


# ==============================
# CLEAN DATA
# ==============================

def clean_data(df):

    df = df.copy()

    # ==============================
    # FIX ENCODING
    # ==============================

    text_columns = [

        "department",
        "title",
        "brand",
        "categories"

    ]

    for col in text_columns:

        if col in df.columns:

            df[col] = df[col].apply(
                fix_encoding
            )

    # ==============================
    # RATING
    # ==============================

    if "rating" in df.columns:

        df["rating"] = pd.to_numeric(

            df["rating"],
            errors="coerce"

        )

    # ==============================
    # PRICE
    # ==============================

    for col in [

        "initial_price",
        "final_price"

    ]:

        if col in df.columns:

            df[col] = (

                df[col]

                .astype(str)

                .str.replace(

                    r"[^\d.]",

                    "",

                    regex=True
                )
            )

            df[col] = pd.to_numeric(

                df[col],

                errors="coerce"
            )

    # ==============================
    # DISCOUNT
    # ==============================

    if "discount" in df.columns:

        df["discount"] = (

            df["discount"]

            .astype(str)

            .str.extract(r'(\d+)')

        )

        df["discount"] = pd.to_numeric(

            df["discount"],

            errors="coerce"

        )

    # ==============================
    # ROOT_BS_RANK
    # ==============================

    if "root_bs_rank" in df.columns:

        df["root_bs_rank"] = (

            df["root_bs_rank"]

            .astype(str)

            .str.extract(r'(\d+)')

        )

        df["root_bs_rank"] = pd.to_numeric(

            df["root_bs_rank"],

            errors="coerce"

        )

    # ==============================
    # FILL MISSING VALUES
    # ==============================

    if "brand" in df.columns:

        df["brand"] = (
            df["brand"]
            .fillna("Unknown")
        )

    if "description" in df.columns:

        df["description"] = (
            df["description"]
            .fillna("")
        )

    if "department" in df.columns:

        df["department"] = (
            df["department"]
            .fillna("Unknown")
        )

    if "categories" in df.columns:

        df["categories"] = (
            df["categories"]
            .fillna("Unknown")
        )

    if "rating" in df.columns:

        df["rating"] = (
            df["rating"]
            .fillna(
                df["rating"].mean()
            )
        )

    if "final_price" in df.columns:

        df["final_price"] = (
            df["final_price"]
            .fillna(
                df["final_price"].median()
            )
        )

    return df