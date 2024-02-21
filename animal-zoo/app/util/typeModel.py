from sqlalchemy.ext.declarative import declarative_base
from app.util.SessionFlaskModel import SessionFlaskModel
from typing import TypeVar

typeModel= TypeVar("typeModel", bound= SessionFlaskModel.getSession().Model)