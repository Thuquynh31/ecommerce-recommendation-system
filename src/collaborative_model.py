import numpy as np
import pandas as pd

from sklearn.neighbors import (
    NearestNeighbors
)

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error
)


# ==============================
# SIMULATE USER INTERACTIONS
# ==============================

def simulate_user_interactions(
    df,
    num_users=100,
    interactions_per_user=20
):

    np.random.seed(42)

    interaction_data = []

    for user_id in range(
        1,
        num_users + 1
    ):

        sampled_products = df.sample(
            interactions_per_user
        )

        for _, row in sampled_products.iterrows():

            interaction_data.append({

                "user_id": user_id,

                "title": row["title"],

                "rating": row["rating"]

            })

    interactions_df = pd.DataFrame(
        interaction_data
    )

    return interactions_df


# ==============================
# CREATE USER-ITEM MATRIX
# ==============================

def create_user_item_matrix(
    interactions_df
):

    user_item_matrix = pd.pivot_table(

        interactions_df,

        index="user_id",

        columns="title",

        values="rating",

        fill_value=0
    )

    return user_item_matrix


# ==============================
# TRAIN KNN MODEL
# ==============================

def train_knn_model(
    user_item_matrix
):

    model_knn = NearestNeighbors(

        metric='cosine',

        algorithm='brute'
    )

    model_knn.fit(
        user_item_matrix
    )

    return model_knn


# ==============================
# FIND SIMILAR USERS
# ==============================

def find_similar_users(
    model_knn,
    user_item_matrix,
    query_index=10,
    n_neighbors=5
):

    distances, indices_knn = (

        model_knn.kneighbors(

            user_item_matrix.iloc[
                query_index,
                :
            ].values.reshape(1, -1),

            n_neighbors=n_neighbors
        )

    )

    print("=" * 50)
    print("SIMILAR USERS")
    print("=" * 50)

    for i in range(

        len(indices_knn.flatten())

    ):

        print(

            f"User: "
            f"{indices_knn.flatten()[i]}, "

            f"Distance: "
            f"{distances.flatten()[i]:.4f}"

        )

    return distances, indices_knn


# ==============================
# EVALUATE COLLABORATIVE MODEL
# ==============================

def evaluate_collaborative(
    interactions_df
):

    # Train-test split
    train_data, test_data = (

        train_test_split(

            interactions_df,

            test_size=0.2,

            random_state=42
        )

    )

    # User mean ratings
    user_mean_rating = (

        train_data.groupby(
            "user_id"
        )["rating"].mean()

    )

    # Predictions
    predictions = []

    for _, row in test_data.iterrows():

        user_id = row["user_id"]

        if user_id in user_mean_rating:

            pred = user_mean_rating[
                user_id
            ]

        else:

            pred = train_data[
                "rating"
            ].mean()

        predictions.append(pred)

    # True ratings
    y_true = test_data["rating"]

    # Predicted ratings
    y_pred = predictions

    # RMSE
    rmse = np.sqrt(

        mean_squared_error(
            y_true,
            y_pred
        )

    )

    # MAE
    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    print("=" * 50)
    print(
        "COLLABORATIVE FILTERING "
        "EVALUATION"
    )
    print("=" * 50)

    print(f"RMSE: {rmse:.4f}")
    print(f"MAE : {mae:.4f}")

    return rmse, mae