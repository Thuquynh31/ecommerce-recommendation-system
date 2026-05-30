import matplotlib.pyplot as plt
import seaborn as sns


# ==============================
# MISSING VALUE HEATMAP
# ==============================

def plot_missing_values(df):

    plt.figure(figsize=(10,6))

    sns.heatmap(
        df.isnull(),
        cbar=False
    )

    plt.title(
        "Missing Values Heatmap",
        fontsize=14,
        pad=15
    )

    plt.show()


# ==============================
# RATING DISTRIBUTION
# ==============================

def plot_rating_distribution(df):

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["rating"],
        bins=20
    )

    plt.title(
        "Distribution of Product Ratings",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Rating")
    plt.ylabel("Count")

    plt.show()


# ==============================
# PRICE DISTRIBUTION
# ==============================

def plot_price_distribution(df):

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["final_price"],
        bins=20
    )

    plt.title(
        "Distribution of Product Prices",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Price")
    plt.ylabel("Count")

    plt.show()


# ==============================
# PRICE VS RATING
# ==============================

def plot_price_vs_rating(df):

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        data=df,
        x="final_price",
        y="rating"
    )

    plt.title(
        "Price vs Rating",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Price")
    plt.ylabel("Rating")

    plt.tight_layout()

    plt.show()


# ==============================
# TOP DEPARTMENTS
# ==============================

def plot_top_departments(df):

    top_departments = (
        df["department"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=top_departments.values,
        y=top_departments.index
    )

    plt.title(
        "Top Product Categories",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Number of Products")
    plt.ylabel("Category")

    plt.tight_layout()

    plt.show()


# ==============================
# TOP BRANDS
# ==============================

def plot_top_brands(df):

    top_brands = (
        df["brand"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=top_brands.values,
        y=top_brands.index
    )

    plt.title(
        "Top 10 Most Popular Brands",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Number of Products")
    plt.ylabel("Brand")

    plt.tight_layout()

    plt.show()


# ==============================
# GET POPULAR PRODUCTS
# BY DEPARTMENT
# ==============================

def get_popular_products_by_department(df):

    popular_products = (

        df[
            [
                "asin",
                "root_bs_rank",
                "department"
            ]
        ]

        .dropna()

    )

    # Remove invalid ASIN rows
    popular_products = (

        popular_products[

            popular_products["asin"]

            .apply(

                lambda x:

                isinstance(x, str)

                and not x.startswith("http")

                and len(x) <= 15
            )
        ]
    )

    # Sort by best seller rank
    popular_products = (

        popular_products

        .sort_values(
            "root_bs_rank"
        )

        .groupby(
            "department"
        )

        .head(5)

    )

    return popular_products


# ==============================
# TOP POPULAR PRODUCTS
# BY DEPARTMENT
# ==============================

def plot_popular_products_by_department(df):

    popular_products = (
        get_popular_products_by_department(df)
    )

    top_products = (

        popular_products

        .sort_values(
            "root_bs_rank"
        )

        .head(20)

    )

    plt.figure(figsize=(12,6))

    sns.barplot(

        data=top_products,

        x="root_bs_rank",

        y="asin",

        hue="department"

    )

    plt.title(

        "Top Popular Products by Department",

        fontsize=14,
        pad=15
    )

    plt.xlabel(
        "Best Seller Rank"
    )

    plt.ylabel(
        "Product ASIN"
    )

    plt.legend(

        bbox_to_anchor=(1.05, 1),

        loc="upper left"

    )

    plt.tight_layout()

    plt.show()