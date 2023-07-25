from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    token = fields.String()
    date_created = fields.DateTime()

class MarvelCharacterSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    comics_appeared_in = fields.Integer(required=True)
    super_power = fields.String()
    date_created = fields.DateTime(dump_only=True)
    user_token = fields.String()