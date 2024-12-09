import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("Animation_Movies.csv")

adult_movies = df[df['adult'] == True]
kids_movies = df[df['adult'] == False]

print("Adult Movies Summary:")
print(adult_movies[['vote_average', 'vote_count', 'revenue', 'budget']].describe())

print("\nKids Movies Summary:")
print(kids_movies[['vote_average', 'vote_count', 'revenue', 'budget']].describe())

def extract_genres(dataframe):
    genres_series = dataframe['genres'].dropna().str.split(', ')
    genre_counts = Counter([genre for sublist in genres_series for genre in sublist])
    return pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)

adult_genres = extract_genres(adult_movies)
kids_genres = extract_genres(kids_movies)

print("\nTop Genres in Adult Animated Films:")
print(adult_genres)

print("\nTop Genres in Kids Animated Films:")
print(kids_genres)

df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')  # Handle errors during conversion
df['release_year'] = df['release_date'].dt.year  # Extract year from release_date

adult_movies = df[df['adult'] == True]
kids_movies = df[df['adult'] == False]

adult_trends = adult_movies['release_year'].value_counts().sort_index()
kids_trends = kids_movies['release_year'].value_counts().sort_index()

print("\nAdult Animation Release Trends Over Years:")
print(adult_trends)

print("\nKids Animation Release Trends Over Years:")
print(kids_trends)

plt.figure(figsize=(10, 5))
plt.bar(adult_genres['Genre'], adult_genres['Count'], alpha=0.7, label='Adult')
plt.bar(kids_genres['Genre'], kids_genres['Count'], alpha=0.7, label='Kids')
plt.xticks(rotation=45, ha='right')
plt.title("Genre Comparison Between Adult and Kids Animated Films")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(adult_trends.index, adult_trends.values, label='Adult', marker='o')
plt.plot(kids_trends.index, kids_trends.values, label='Kids', marker='o')
plt.title("Release Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Films")
plt.legend()
plt.show()
