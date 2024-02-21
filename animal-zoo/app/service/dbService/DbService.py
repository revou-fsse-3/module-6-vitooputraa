from app.util.typeModel import typeModel
from app.util.SessionFlaskModel import SessionFlaskModel
from sqlalchemy.exc import SQLAlchemyError

class DbModelService:
    def __init__(self, dbModel:typeModel) -> None:
        self.dbModel= dbModel
        self.dbSession=SessionFlaskModel.getSession().session

    def getDbModalAll( self,) :
        items=self.dbModel.query.all()
        return items

    def postDbModal(self, model:typeModel):
        try:
            self.dbSession.add(model)
            self.dbSession.commit()
        except SQLAlchemyError:
            raise SQLAlchemyError

    def getDbModal(self, store_id: str)->typeModel:
        store = self.dbModel.query.get_or_404(store_id)
        return store
    
    def deleteDbModal(self, store_id: str):
        db = self.getDbModal(store_id)
        self.dbSession.delete(db)
        self.dbSession.commit()
        return
    def updateDbModel(self ,store_id: str, args)->typeModel:
        item=self.getDbModal(store_id)
        if item == None : return 
        item.update(**args)
        self.dbSession.add(item)
        self.dbSession.commit()
        return item



