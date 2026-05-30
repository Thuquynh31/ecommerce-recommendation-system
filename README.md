# E-Commerce Recommendation System

## Giới thiệu

Dự án xây dựng hệ thống đề xuất sản phẩm thương mại điện tử dựa trên dữ liệu sản phẩm Amazon (https://brightdata.com/cp/datasets/browse/gd_l7q7dkf244hwjntr0?id=hl_67a497d9&tab=sam). Hệ thống kết hợp nhiều phương pháp recommendation nhằm hỗ trợ cá nhân hóa trải nghiệm người dùng và cải thiện chất lượng gợi ý sản phẩm.

Các phương pháp được sử dụng gồm:

* Popularity-Based Recommendation
* Content-Based Recommendation
* Collaborative Filtering
* Hybrid Recommendation System

---

## Kỹ thuật sử dụng

* Data Cleaning
* Exploratory Data Analysis (EDA)
* TF-IDF Vectorization
* Cosine Similarity
* K-Nearest Neighbors (KNN)

---

## Đánh giá mô hình

Các mô hình được đánh giá bằng:

* Average Rating@K
* Precision@K
* RMSE
* MAE

---

## Công nghệ sử dụng

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Cấu trúc project

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

## Cách chạy project

### 1. Clone repository

```bash
git clone https://github.com/Thuquynh31/ecommerce-recommendation-system.git
```

### 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 3. Chạy project

```bash
python main.py
```

---

## Hướng phát triển

* Sử dụng dữ liệu tương tác người dùng thực tế
* Cải thiện độ chính xác của hệ thống đề xuất
* Xây dựng giao diện web cho hệ thống
