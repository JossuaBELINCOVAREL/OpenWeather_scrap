from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

def get_books_data():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Erreur de requête", response.status_code)
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = []

    # Scraping des livres
    for book in soup.find_all('article', class_='product_pod'):
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        
        books.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })
    
    return books

@app.route('/')
def index():
    books = get_books_data()
    if books:
        return render_template('index.html', books=books)
    else:
        return "Erreur lors de la récupération des données"

if __name__ == '__main__':
    app.run(debug=True)
