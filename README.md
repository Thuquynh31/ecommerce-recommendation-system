# E-Commerce Recommendation System

## Introduction

This project builds an e-commerce product recommendation system based on Amazon product data from [Bright Data](https://brightdata.com/cp/datasets/browse/gd_l7q7dkf244hwjntr0?id=hl_67a497d9&tab=sam&utm_source=chatgpt.com).
The system combines multiple recommendation approaches to support personalized user experiences and improve product recommendation quality.

The project includes the following recommendation methods:

* Popularity-Based Recommendation
* Content-Based Recommendation
* Collaborative Filtering
* Hybrid Recommendation System

---

## Techniques Used

* Data Cleaning
* Exploratory Data Analysis (EDA)
* TF-IDF Vectorization
* Cosine Similarity
* K-Nearest Neighbors (KNN)

---

## Model Evaluation

The models are evaluated using:

* Average Rating@K
* Precision@K
* RMSE
* MAE

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Project Structure

```bash
ecommerce-recommendation-system/

├── data/
│   └── amazon_products.csv
│
├── notebooks/
│   └── recommendation_system.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── popularity_model.py
│   ├── content_based_model.py
│   ├── collaborative_model.py
│   └── hybrid_model.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Thuquynh31/ecommerce-recommendation-system.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

---

## Future Improvements

* Use real user interaction data
* Improve recommendation accuracy
* Build a web interface for the system
