from app.service.dbService.DbService import DbService
from app.model.baseModel.AnimalModel import AnimalModel

class AnimalModelService:
    @staticmethod
    def getDb()-> DbService :
        dbAnimal = DbService(AnimalModel)
        return dbAnimal