from flask import Flask, request, jsonify
from config.database import engine, Base
from flask_cors import CORS

from app.models.usuario import Usuario
from app.models.favorito import Favorito 

from app.controllers.usuario_controller import *
from app.controllers.favorito_controller import *

from app.services.recomendador_service import recomendar_titulo
from app.services.omdb_service import buscar_pelicula

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API funcionando"

@app.route('/usuarios', methods=['POST'])
def crear():
    data = request.json
    usuario = crear_usuario(data)

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    })

@app.route('/usuarios', methods=['GET'])
def listar():
    usuarios = obtener_usuarios()

    return jsonify([
        {
            "id": u.id,
            "nombre": u.nombre,
            "email": u.email
        } for u in usuarios
    ])


@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = obtener_usuario_id(id)

    if not usuario:
        return jsonify({
            "error": "usuario no encontrado"
        }), 404
    
    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    })

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar(id):
    data = request.json

    usuario = actualizar_usuario(id,data)

    if not usuario:
        return jsonify({
            "error": "usuario no encontrado"
        }), 404
    
    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    })


@app.route('/favoritos', methods=['POST'])
def agregar_fav():
    data = request.json
    fav = agregar_favorito(data)

    return jsonify({"mensaje": "Guardado en favoritos"})


@app.route('/favoritos/<int:usuario_id>', methods=['GET'])
def ver_favoritos(usuario_id):
    favoritos = obtener_favoritos(usuario_id)

    return jsonify([
        {
            "id": f.id,
            "titulo": f.titulo
        } for f in favoritos
    ])

@app.route('/favoritos/<int:id>', methods=['DELETE'])
def eliminar_fav(id):
    eliminado = elminar_favorito(id)

    if not eliminado:
        return jsonify({
            "error": "Favorito no encontrado"
        }), 404
    
    return jsonify({
        "mensaje": "Favorito eliminado"
    })

@app.route('/recomendar', methods=['GET'])
def recomendar():
    estado = request.args.get("estado")

    titulos = recomendar_titulo(estado)

    if not titulos:
        return jsonify({
            "error": "Estado de animo no valido"
        }), 400
    
    peliculas = []
    
    for titulo in titulos:
        pelicula = buscar_pelicula(titulo)

        peliculas.append({
            "titulo": pelicula["Title"],
            "año": pelicula["Year"],
            "genero": pelicula["Genre"],
            "sinopsis": pelicula["Plot"],
            "calificacion": pelicula["imdbRating"],
            "poster": pelicula["Poster"]  
        })

    return jsonify(peliculas)


@app.route('/inicio', methods=['GET'])
def inicio():
    titulos = [
        "Shrek",
        "Toy Story",
        "Titanic",
        "Avatar",
        "Interstellar",
        "The Matrix",
        "John Wick",
        "Gladiator",
        "The Dark Knight",
        "Inception",
        "Cars",
        "Finding Nemo",
        "Coco",
        "Up",
        "Frozen",
        "Joker",
        "Fight Club",
        "The Godfather",
        "Forrest Gump",
        "Top Gun"
    ]

    peliculas = []

    for titulo in titulos:
        pelicula = buscar_pelicula(titulo)

        peliculas.append({
            "titulo": pelicula["Title"],
            "año": pelicula["Year"],
            "genero": pelicula["Genre"],
            "sinopsis": pelicula["Plot"],
            "calificacion": pelicula["imdbRating"],
            "poster": pelicula["Poster"]
        })
    
    return jsonify(peliculas)

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    usuario = login_usuario(
        data["email"],
        data["password"]
    )

    if not usuario:

        return jsonify({
            "error": "Credenciales inválidas"
        }), 401

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    })


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)