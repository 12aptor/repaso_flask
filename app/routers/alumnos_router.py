from app import app

@app.route("/alumnos")
def alumnos():
  return "Esta es la ruta alumnos 😁"