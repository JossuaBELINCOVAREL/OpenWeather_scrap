import requests
from bs4 import BeautifulSoup
import pandas as pd

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
        availability = book.find('p', class_='instock availability').text.strip()
        
        books.append({
            'Title': title,
            'Availability': availability
        })
    
    return books

def save_books_to_csv(books):
    df = pd.DataFrame(books)
    df.to_csv('books.csv', index=False)
    print("Fichier CSV créé avec succès !")
