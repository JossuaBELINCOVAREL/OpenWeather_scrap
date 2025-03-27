from flask import Flask, render_template, send_file
from scraper import get_books_data, save_books_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    books = get_books_data()
    if books:
        save_books_to_csv(books)  # Sauvegarde le fichier CSV
        return render_template('index.html', books=books)
    else:
        return "Erreur lors du scraping", 500

@app.route('/download')
def download():
    return send_file('books.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
