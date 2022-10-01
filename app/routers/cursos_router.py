from app import app
from app.controllers.cursos_controller import CursoController

@app.route("/cursos")
def cursos():
  listaCursos = CursoController()
  return listaCursos.getAll()