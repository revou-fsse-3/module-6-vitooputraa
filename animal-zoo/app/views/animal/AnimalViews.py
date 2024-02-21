from flask.views import MethodView
from flask_smorest import Blueprint, abort
from app.schemas.AnimalSchemas import AnimalSchemasWithId,AnimalSchemas
from app.service.dbService.AnimalService import AnimalService

blp = Blueprint("Animals",  __name__, description="Animals route ")

@blp.route("/animal/<string:item_id>")
class AnimalViews(MethodView):
        
    @blp.response(200, AnimalSchemasWithId)
    def get(self, item_id):
        print(item_id)
        return AnimalService.getDb().getDbModal(item_id)
    
    @blp.arguments(AnimalSchemas(partial=("name","species","gender","age")))
    @blp.response(200, AnimalSchemasWithId)
    def put(self ,item_data,item_id):
        items= AnimalService.getDb().updateDbModel(item_id ,item_data)
        return items
        
    def delete(self,item_id ):
        AnimalService.getDb().deleteDbModal(item_id)
        return {"message": "Item deleted."}