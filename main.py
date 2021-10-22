from flask import Flask, jsonify, request
from storage import allmovies, likedmovies, dislikedmovies, notwatched
from demofilter import output
from content import getrecommendations

app = Flask(__name__)

@app.route('/get-movie')
def getmovie():
    moviedata ={
        'title':allmovies[0][19], 'release_date':allmovies[0][13], 'duration':allmovies[0][15], 'rating':allmovies[0][20], 'overview':allmovies[0][9],
    }    
    return jsonify({ 'data':moviedata, 'status':'success'})

@app.route('/liked-movie', methods = ['POST'])
def likedmovies():
    movie = allmovies[0]
  #  allmovies = allmovies[1:]
    likedmovies.append(movie)
    allmovies.pop(0)
    return jsonify({ 'status':'success'})

@app.route('/disliked-movie', methods = ['POST'])
def dislikedmovies():
    movie = allmovies[0]
    #allmovies = allmovies[1:]
    dislikedmovies.append(movie)
    allmovies.pop[0]
    return jsonify({ 'status':'success'}) 

@app.route('/notwatched-movie', methods = ['POST'])
def notwatched():
    movie = allmovies[0]
   # allmovies = allmovies[1:]
    notwatched.append(movie)
    allmovies.pop[0]
    return jsonify({ 'status':'success'})    

@app.route('/popular-movies')
def popmovies():
    moviedata = []
    for i in output:
        _d ={'title':i[0],'release_date':i[1],'duration':i[2],'rating':i[3],'overview':i[4]}    
        moviedata.append(_d)
    return jsonify({ 'data':moviedata, 'status':'success'})     

@app.route('/recommended-movies')
def recommovie():
    allrecommended = []
    for likedmovie in likedmovies:
        output = getrecommendations(likedmovie[19])
        for data in output:
            allrecommended.append(data)
    import itertools
    allrecommended.sort()
    allrecommended = list(allrecommended for allrecommended,_ in itertools.groupby(allrecommended) )
    moviedata = []
    for recommended in allrecommended:
        _d ={'title':recommended[0],'release_date':recommended[1],'duration':recommended[2],'rating':recommended[3],'overview':recommended[4]}    
        moviedata.append(_d)
    return jsonify({ 'data':moviedata, 'status':'success'})  
















if __name__ == '__main__':
    app.run()