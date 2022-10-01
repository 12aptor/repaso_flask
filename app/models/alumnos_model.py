from sqlalchemy import Column, Integer, String, Boolean
from app import db

class AlumnoModel(db.Model):
  __tablename__ = 'alumnos'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(200))
  dni = Column(String(8))
  edad = Column(Integer)
  estado = Column(Boolean, default=True)
  
  curso_id = Column(Integer, db.ForeignKey('cursos.id'))
  curso = db.relationship('CursoModel')