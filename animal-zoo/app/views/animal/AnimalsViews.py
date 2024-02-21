from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas.AnimalSchemas import AnimalSchemas,AnimalSchemasWithId
from app.model.baseModel.AnimalModel import AnimalModel
from app.service.dbService.AnimalService import AnimalService

blp = Blueprint("Animal", __name__, description="Animal route ")


@blp.route("/animals")
class AnimalsViews(MethodView):
    
    @blp.response(200, AnimalSchemasWithId(many=True))
    def get(self):
        items=AnimalService.getDb().getDbModalAll()
        return items
    
    @blp.arguments(AnimalSchemas)
    @blp.response(201, AnimalSchemasWithId)
    def post(self ,item_data):
        items=AnimalModel(**item_data)
        AnimalService.getDb().postDbModal(items)
        return items