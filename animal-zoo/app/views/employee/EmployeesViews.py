from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas.EmployeeSchemas import EmployeeSchemas,EmployeeSchemasWithId
from app.model.baseModel.EmployeeModel import EmployeeModel
from app.service.dbService.EmployeeService import EmployeeService

blp = Blueprint("employees",  __name__, description="employees route ")

@blp.route("/employees")
class EmployeesViews(MethodView):
    
    @blp.response(200, EmployeeSchemasWithId(many=True))
    def get(self):
        return EmployeeService.getDb().getDbModalAll()
    
    @blp.arguments(EmployeeSchemas)
    @blp.response(200, EmployeeSchemasWithId)
    def post(self ,  item_data):
        items=EmployeeModel(**item_data)
        EmployeeService.getDb().postDbModal(items)
        return items