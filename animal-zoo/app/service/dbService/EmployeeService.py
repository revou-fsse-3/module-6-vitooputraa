from app.service.dbService.DbService import DbService
from app.model.baseModel.EmployeeModel import EmployeeModel

class EmployeeModelService:
    @staticmethod
    def getDb()-> DbService :
        dbAnimal = DbService(EmployeeModel)
        return dbAnimal