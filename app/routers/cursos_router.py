from app import app
from app.controllers.cursos_controller import CursoController
from flask import request

@app.route("/cursos", methods=['GET', 'POST'])
def cursos():
  if request.method == 'GET':
    listaCursos = CursoController()
    return listaCursos.getAll()
  else:
    json_input = request.get_json()
    nuevoCurso = CursoController()
    return nuevoCurso.post(json_input)