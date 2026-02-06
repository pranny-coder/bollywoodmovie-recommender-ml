# 🎬 Bollywood Movie Recommendation System (ML Project)

## 📌 Project Overview

This project builds a **Bollywood movie recommendation system** using machine learning.
It recommends similar movies based on genre, cast, director, and movie overview.

If a user enters a movie name, the system suggests top similar Bollywood movies — similar to Netflix/Amazon recommendation systems.

---

## 🚀 Features

* Recommends similar Bollywood movies
* Uses content-based filtering
* Combines genre, cast, director & overview
* Cosine similarity for recommendations
* Interactive user input system

---

## 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* CountVectorizer
* Cosine Similarity

---

## ⚙️ How It Works

1. Movie features (genre, cast, director, overview) are combined into a single text column.
2. Text is converted into numeric vectors using **CountVectorizer**.
3. Cosine similarity calculates similarity between movies.
4. When user enters a movie name → system recommends most similar movies.

---

## 📊 Dataset

Dataset not uploaded due to size.

Place:

```
movies.csv
```

inside project folder before running.

Dataset contains:

* movie_name
* genre
* director
* cast
* overview

---

## ▶️ How to Run

Install required libraries:

```
pip install pandas scikit-learn
```

Run program:

```
python recommender.py
```

Enter movie name when prompted:

```
Enter a movie name: Jawan
```

System will display recommended movies.

---

## 🎯 Learning Outcomes

* Content-based recommendation systems
* Text vectorization using CountVectorizer
* Cosine similarity
* Feature engineering for ML
* Real-world recommender system logic

---

## 👨‍💻 Author

Pranav
