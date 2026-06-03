from config.database import SessionLocal
from app.models.favorito import Favorito

def agregar_favorito(data):
    db =  SessionLocal()

    favorito =  Favorito(
        usuario_id=data["usuario_id"],
        titulo=data["titulo"]
    )

    db.add(favorito)
    db.commit()
    db.close()

    return favorito

def obtener_favoritos(usuario_id):
    db = SessionLocal()
    favoritos = db.query(Favorito).filter(Favorito.usuario_id == usuario_id).all()
    db.close()
    return favoritos