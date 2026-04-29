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
        "email": "amen@gmail.com",
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