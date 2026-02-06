import pandas as pd
df=pd.read_csv("movies.csv")

df=df[["movie_name","genre","director","cast","overview"]]

df["tags"] = df["genre"] + " " + df["director"] + " " + df["cast"] + " " + df["overview"]

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words="english")
vectors=cv.fit_transform(df["tags"]).toarray()

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

def recommend(movie):
    movie = movie.lower()
    
    idx = df[df["movie_name"].str.lower() == movie].index
    
    if len(idx) == 0:
        print("Movie not found")
        return
    
    idx = idx[0]
    
    distances = list(enumerate(similarity[idx]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    
    print("\n🎬 Recommended movies:\n")
    
    count = 1
    for i in movies_list:
        print(f"{count}. {df.iloc[i[0]].movie_name}")
        count += 1


movie=input("Enter a movie name: ")
recommend(movie)