from app import app
from app.controllers.alumnos_controller import AlumnoController

@app.route("/alumnos", methods=['GET'])
def alumnos():
  listaAlumnos = AlumnoController()
  return listaAlumnos.getAll()