from app import app


@app.route("/cursos")
def cursos():
  return "Esta es la ruta cursos 😃"