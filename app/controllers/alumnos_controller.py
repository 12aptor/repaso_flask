from app.models.alumnos_model import AlumnoModel
from app.schemas.alumnos_schema import AlumnoSchema

class AlumnoController():
  def __init__(self):
    self.model = AlumnoModel
    self.schema = AlumnoSchema

  def getAll(self):
    alumnos = self.model.query.all()
    response = self.schema(many=True)
    return response.dump(alumnos), 200