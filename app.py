from flask import Flask, render_template
from scraper import get_trending_movies

# import de la fonction get_trending_movies qui va scrapper les films

app = Flask(__name__)

@app.route('/') # route pour afficher la page HTML avec la liste des films
def index():
    trending_movies = get_trending_movies()
    return render_template('index.html', movies=trending_movies)
    # trending_movies = ["Movie 1", "Movie 2", "Movie 3"]
    # return render_template('index.html', movies=trending_movies)

if __name__ == '__main__':
    app.run(debug=True)
