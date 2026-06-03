import requests

API_KEY = "811f14ac"

def buscar_pelicula(titulo):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={titulo}"

    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    return response.json()