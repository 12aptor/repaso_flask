from urllib import response
from app.models.cursos_model import CursoModel
from app.schemas.cursos_schema import CursoSchema

class CursoController():
  def __init__(self):
    self.model = CursoModel
    self.schema = CursoSchema
  
  def getAll(self):
    cursos = self.model.query.all()
    response = self.schema(many=True)
    return response.dump(cursos), 200