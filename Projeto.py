# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv", index_col = 0)


netflix_subset = netflix_df[netflix_df["type"]=="Movie"]


netflix_movies = netflix_subset[["title",'country','genre','release_year','duration']]


short_movies = netflix_movies[netflix_movies['duration']<60]


colors = []
for lab,row in netflix_movies.iterrows():
    if row['genre'] == "Documentaries":
        colors.append('green')
    elif row['genre'] == 'Stand-Up':
        colors.append('yellow')
    elif row['genre'] == 'Children':
        colors.append('blue')
    else:
        colors.append('red')
        
        
x = netflix_movies['release_year']
y = netflix_movies['duration']
fig = plt.figure(figsize=(12,8))
plt.scatter(x ,y, c=colors, alpha = 0.8)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")


answer = "no"
print("Temos certeza de que os filmes estão ficando mais curtos? "+ answer)
