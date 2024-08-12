from schema import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=True, validate=validate.Length(min=1))
    password = fields.String(required=True, validate=validate.Length(min=1))
    role = fields.String(required=False)

User_schema= UserSchema()
Users_schema= UserSchema(many=True)