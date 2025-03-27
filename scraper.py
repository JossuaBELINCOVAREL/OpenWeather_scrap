import requests
from bs4 import BeautifulSoup

def get_trending_movies():
    url = 'https://www.imdb.com/chart/moviemeter/'
    response = requests.get(url)
    
    # Si la requête échoue, retourne une liste vide
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver la liste des films tendance avec la classe mise à jour
    movie_list = soup.find_all('li', class_='ipc-metadata-list-summary-item')

    movies = []

    # Parcourir chaque élément de film dans la liste
    for movie in movie_list:
        # Extraire le titre du film
        title = movie.find('span', class_='sc-16ede6d9-2 knbZAA')  # Assurez-vous de mettre la bonne classe ici pour le titre
        if title:
            title = title.get_text(strip=True)
        
        # Extraire le rang ou la position (si disponible)
        rank = movie.find('span', class_='ipc-metadata-list-item__label')  # Mettez la bonne classe ici pour le rang
        if rank:
            rank = rank.get_text(strip=True)
        
        if title and rank:
            movies.append(f"{rank} - {title}")

    return movies
