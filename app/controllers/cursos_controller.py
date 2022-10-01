from urllib import response
from app.models.cursos_model import CursoModel
from app.schemas.cursos_schema import CursoSchema
from marshmallow import ValidationError
from app import db

class CursoController():
  def __init__(self):
    self.model = CursoModel
    self.curso_schema = CursoSchema()
    self.cursos_schema = CursoSchema(many=True)
  
  def getAll(self):
    cursos = self.model.query.all()
    return self.cursos_schema.dump(cursos), 200


  def post(self, json_input):
    if not json_input:
      return {'message': 'Datos de entrada no proporcionados'}, 400

    try:
      data = self.curso_schema.load(json_input)
      curso = self.model(**data)
      db.session.add(curso)
      db.session.commit()

      resultado = self.curso_schema.dump(curso)
      return resultado, 201

    except ValidationError as err:
      db.session.rollback()
      return err.messages, 500