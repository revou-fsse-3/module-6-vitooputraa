from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.EmployeeSchemas import EmployeeSchemas,EmployeeSchemasWithId
from service.dbService.EmployeeService import EmployeeService
blp = Blueprint("employee",  __name__, description="employees route ")

@blp.route("/employee/<string:item_id>")
class AnimalViews(MethodView):
        
    @blp.response(200, EmployeeSchemasWithId)
    def get(self, item_id: str):
        return EmployeeService.getDb().getDbModal(item_id)
    
    @blp.arguments(EmployeeSchemas(partial=("name", "role", "schedule", "email","phone")))
    @blp.response(200, EmployeeSchemasWithId)
    def put(self ,item_data,item_id):
        items= EmployeeService.getDb().updateDbModel(item_id,item_data )
        return items
        
    def delete(self,item_id ):
        EmployeeService.getDb().deleteDbModal(item_id)
        return {"message": "Item deleted."}