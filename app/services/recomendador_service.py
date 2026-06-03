import random

peliculas_por_estado = {

    "feliz": [
        "The Hangover",
        "Toy Story",
        "Shrek"
    ],

    "triste": [
        "The Pursuit of Happyness",
        "Forrest Gump",
        "The Green Mile"
    ],

    "romantico": [
        "Titanic",
        "The Notebook",
        "La La Land"
    ],

    "emocionado": [
        "Avengers Endgame",
        "Mad Max Fury Road",
        "John Wick"
    ],

    "miedo": [
        "The Conjuring",
        "Insidious",
        "It"
    ]
}

def recomendar_titulo(estado):
    peliculas = peliculas_por_estado.get(
        estado.lower()
    )

    if not peliculas:
        return None
    
    return random.choice(peliculas)