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

    usuario = db.query( Usuario).filter(Usuario.id == id).first()

    if usuario:
        db.delete(usuario)
        db.commit()

    db.close()


def obtener_usuario_id(id):

    db = SessionLocal()

    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    db.close()

    return usuario


def actualizar_usuario(id, data):

    db = SessionLocal()

    usuario = db.query( Usuario).filter(Usuario.id == id).first()

    if not usuario:
        db.close()
        return None

    usuario.nombre = data["nombre"]

    usuario.email = data["email"]

    db.commit()
    db.refresh(usuario)
    db.close()

    return usuario


def login_usuario(email, password):

    db = SessionLocal()

    usuario = db.query(Usuario).filter(Usuario.email == email,Usuario.password == password).first()
    db.close()

    return usuario