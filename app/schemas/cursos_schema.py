from marshmallow import Schema, fields

class CursoSchema(Schema):
  id = fields.Integer(dump_only=True)
  nombre = fields.String(required=True)
  estado = fields.Boolean(dump_only=True)