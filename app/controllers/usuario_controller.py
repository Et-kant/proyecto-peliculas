from config.database import SessionLocal
from app.models.usuario import Usuario

def crear_usuario(data):
    db = SessionLocal()

    usuario = Usuario(
        nombre=data["nombre"],
        email=data["email"],
        password=data["password"]
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    db.close()

    return usuario


def obtener_usuarios():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    db.close()
    return usuarios

def eliminar_usuario(id):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if usuario:
        db.delete()
        db.commit()
        db.close()