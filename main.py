from flask import Flask, request, jsonify
from config.database import engine, Base

from app.models.usuario import Usuario
from app.models.favorito import Favorito 

from app.controllers.usuario_controller import *
from app.controllers.favorito_controller import *

app = Flask(__name__)

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


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)