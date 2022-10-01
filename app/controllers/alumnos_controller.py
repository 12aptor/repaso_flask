from app.models.alumnos_model import AlumnoModel
from app.schemas.alumnos_schema import AlumnoSchema
from marshmallow import ValidationError
from app import db

class AlumnoController():
  def __init__(self):
    self.model = AlumnoModel
    self.alumno_schema = AlumnoSchema()
    self.alumnos_schema = AlumnoSchema(many=True)

  def getAll(self):
    alumnos = self.model.query.all()
    return self.alumnos_schema.dump(alumnos), 200

  def post(self, json_input):
    if not json_input:
      return {"message": "Datos de entrada no proporcinados"}, 400
    try:
      data = self.alumno_schema.load(json_input)
      alumno = self.model(**data)
      db.session.add(alumno)
      db.session.commit()

      result = self.alumno_schema.dump(alumno)
      return result, 201
    except ValidationError as err:
      db.session.rollback()
      return err.messages, 500