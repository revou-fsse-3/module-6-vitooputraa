from app.util.SqlPhat import getSqlPhat
from flask_sqlalchemy import SQLAlchemy

class SessionFlaskModel:
    session:SQLAlchemy= None
    def getSession()-> SQLAlchemy:
        if SessionFlaskModel.session== None:        
            SessionFlaskModel.session= SQLAlchemy()
        return SessionFlaskModel.session