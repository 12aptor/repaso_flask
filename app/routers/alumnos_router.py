from app import app
from app.controllers.alumnos_controller import AlumnoController
from flask import request

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
  if request.method == 'GET':
    listaAlumnos = AlumnoController()
    return listaAlumnos.getAll()
  else:
    json_input = request.get_json()
    nuevoAlumno = AlumnoController()
    return nuevoAlumno.post(json_input)