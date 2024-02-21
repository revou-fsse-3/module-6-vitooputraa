from marshmallow import Schema, fields

class AnimalSchemas(Schema):
    name= fields.Str()
    species=fields.Str()
    gender=fields.Str()
    age= fields.Int()
    
class AnimalSchemasWithId(AnimalSchemas):
    animaId= fields.Str(dump_only=True)
