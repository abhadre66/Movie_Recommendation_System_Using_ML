# 🎬 Movie Recommender System Using Machine Learning

<img src="demo/6.jpeg" alt="workflow" width="70%">

## 📌 Overview  
Recommendation systems have become increasingly valuable in today’s fast-paced world. With so many tasks to complete in limited time, people rely on such systems to make quick and effective choices without putting in extra mental effort.

The main goal of a recommendation system is to identify content that matches a user’s interests. It considers multiple factors to generate personalized lists of movies or items tailored to each individual. These systems use Artificial Intelligence algorithms to filter through countless options and highlight the most relevant ones. The recommendations are influenced by a user’s profile, browsing history, viewing habits of similar users, and the likelihood of enjoying certain content. This is made possible through predictive modeling and heuristic techniques applied to the available data.

---

## ⚡ New Feature Update
I added a powerful new feature:  

- After movies are recommended, each movie now shows the **platform(s)** where it’s available.  
- Clicking on a movie redirects you to its **TMDB page**.  
- TMDB provides detailed availability info:  
  - Free to watch  
  - Rent options  
  - Streaming platforms  
- If the movie is available on a streaming platform (e.g., Netflix, Prime Video, Disney+), you can **directly navigate to that platform** from TMDB.  

---

## 🔎 Types of Recommendation Systems  

### 1. Content-Based Filtering  
- Uses item attributes (genres, cast, etc.) to suggest similar items.  
- Example: YouTube, Twitter recommendations.  
- Works by creating embeddings/vectors of features.  
- Limitation: Can lead to over-specialization (recommends only very similar items).  

### 2. Collaborative Filtering  
- Based on user-item interactions (ratings, comments).  
- Groups users with similar preferences into clusters.  
- Example: Book recommendations.  
- Limitation:  
  - Computationally expensive (large user-item matrix).  
  - Tends to recommend only popular items.  
  - New/unrated items may not get recommended.  

### 3. Hybrid Systems  
- Combines **content-based** and **collaborative filtering** approaches.  
- More effective in modern systems.  
- Techniques used: word2vec, embeddings, etc.  

---

## 🖥️ Project Demo  

<img src="demo/1.png" alt="workflow" width="70%">  
<img src="demo/2.png" alt="workflow" width="70%">  

---

## 📊 Dataset  

We use the **TMDB 5000 Movie Dataset** available on Kaggle:  
👉 [Dataset Link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)  

---

## 🧠 Core Concept: Cosine Similarity  

- Cosine similarity measures how similar two vectors are.  
- Formula returns a value between **0 and 1**:  
  - `0` → completely different  
  - `1` → completely similar  
- Used here to compare movies based on their feature vectors.  

More details: [Cosine Similarity Explained](https://www.learndatasci.com/glossary/cosine-similarity/)  

---

## ⚙️ Installation & Setup  

### 1. Clone the repository  
```bash
git clone https://github.com/abhadre66/Movie-Recommender-System-Using-Machine-Learning.git
cd Movie-Recommender-System-Using-Machine-Learning


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/abhadre66/Movie-Recommender-System-Using-Machine-Learning.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n movie python=3.7.10 -y
```

```bash
conda activate movie
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
#run this file to generate the models

Movie Recommender System Data Analysis.ipynb
```

Now run,
```bash
streamlit run app.py
```


```bash
Author: Abhishek Bhadre
Email: abhadre06@gmail.com

```
