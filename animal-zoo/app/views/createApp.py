from flask import Flask, jsonify
from flask_smorest import Api
from app.util.SessionFlaskModel import SessionFlaskModel
from app.util.SqlPhat import getSqlPhat
from app.views.animal.AnimalsViews import app as AnimalsViews
from app.views.animal.AnimalViews import app as AnimalViews
from app.views.employee.EmployeesViews import app as EmployeesViews
from app.views.employee.EmployeeViews import app as EmployeeViews

def create_app(db_url=none):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Animal Zoo API "
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or getSqlPhat()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    
    db= SessionFlaskModel.getSession()
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    api = Api(app)
    
    api.register_blueprint(AnimalsViews)
    api.register_blueprint(AnimalViews)
    api.register_blueprint(EmployeesViews)
    api.register_blueprint(EmployeeViews)
    
    return app