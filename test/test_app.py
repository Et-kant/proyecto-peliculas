import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_crear_usuario(client):
    response = client.post("/usuarios", json = {
        "nombre" : "test",
        "email": "amen1@gmail.com",
        "password": "1234"
    })

    assert response.status_code == 200
    data = response.get_json()

    assert "id" in data
    assert data ["nombre"] == "test"


def test_obtener_usuarios(client):
    response = client.get('/usuarios')

    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)


def test_agregar_favorito(client):
    usuario = client.post("/usuarios", json={
        "nombre": "test",
        "email": "email1@test.com",
        "password": "1234"
    })

    usuario_data = usuario.get_json()

    response = client.post("/favoritos", json={
        "usuario_id" : usuario_data["id"],
        "titulo": "Batman"
    })

    assert response.status_code == 200