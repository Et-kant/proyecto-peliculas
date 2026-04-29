from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base

class Favorito(Base):
    __tablename__ = "favoritos"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    titulo = Column(String)