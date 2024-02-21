from marshmallow import Schema, fields

class EmployeeSchemas(Schema):
    role= fields.Str()
    schedule= fields.Str()
    name=fields.Str()
    email= fields.Str() 
    phone= fields.Str()


class EmployeeSchemasWithId(EmployeeSchemas):
    employeeId= fields.Str(dump_only=True)

