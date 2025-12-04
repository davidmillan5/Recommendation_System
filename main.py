# Popularity-Based Filtering

import pandas as pd
movies = pd.read_csv("movies.csv")
credits_var = pd.read_csv("credits.csv")
ratings = pd.read_csv("ratings.csv")

#print(movies.head())

# Calculate a weighted rating
"""
WR = (v ÷ (v+m)) x R + (m ÷ (v+m)) x C
v - number of votes for a movie
m - minimum number of votes required
R - average rating of the movie
C - average rating across all movies
"""

m = movies["vote_count"].quantile(0.9)
#print(m)

C = movies["vote_average"].mean()
#print(C)

movies_filtered = movies.loc[movies["vote_count"] >= m].copy()

def weighted_rating(df, m=m, C=C):
    """ """
    R = df["vote_average"]
    v = df["vote_count"]
    wr = ((v / (v+m)) * R) + ((m / (v+m)) * C)
    return wr

movies["weighted_rating"] = movies.apply(weighted_rating, axis=1)