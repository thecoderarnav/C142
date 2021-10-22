import csv
allmovies = []

with open('movies.csv',encoding ='utf8' )as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

likedmovies = []
dislikedmovies = []
notwatched = []