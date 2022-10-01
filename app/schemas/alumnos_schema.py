from marshmallow import Schema, fields
from app.helpers.error_helper import campo_necesario

class AlumnoSchema(Schema):
  id = fields.Integer(dump_only=True)
  nombre = fields.String(required=True, validate=campo_necesario)
  dni = fields.String(required=True, validate=campo_necesario)
  edad = fields.Integer(required=True, validate=campo_necesario)
  estado = fields.Boolean(dump_only=True)
  curso_id = fields.Integer(required=True, validate=campo_necesario)