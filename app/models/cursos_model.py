from app import db
from sqlalchemy import Column, Integer, Boolean, String

class CursoModel(db.Model):
  __tablename__ = 'cursos'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100))
  estado = Column(Boolean, default=True)

  