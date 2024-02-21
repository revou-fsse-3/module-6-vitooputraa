from util.SessionFlaskModel import SessionFlaskModel
from uuid import uuid4
from app.model.Species import AnimalSpecies
from app.model.Sex import Gender
from app.model.Species import AnimalSpecies
from app.service.MemberService import EnumMemberService
from dataclasses import dataclass

db= SessionFlaskModel.getSession()

class AnimalBaseModel(db.Model,):
    __tablename__= "animal"
    animaId= db.Column("animal_id", db.String, primary_key=True)
    name= db.Column("name", db.String)
    species= db.Column("species", db.String)
    gender= db.Column("gender", db.String)
    age= db.Column("age" , db.Integer)

    def __init__(self, name: str ,species: str, gender:str, age:int ):
        self.animaId=str(uuid4())
        self.name=name
        self.species=EnumMemberService(AnimalSpecies).getMatchValue(species)
        self.gender=EnumMemberService(Gender).getMatchValue(gender)
        self.age=age

    def update(self, name: str=None ,species: str=None, gender:str=None, age:int=None ):
        self.name=name if name != None else self.name
        self.species=EnumMemberService(AnimalSpecies).getMatchValue(species) if species != None else self.species
        self.gender=EnumMemberService(Gender).getMatchValue(gender) if gender != None else self.gender
        self.age=age if age != None else self.age
    
    def __str__ (self):
        return f"{self.species} {self.name} {self.gender} {self.age}"
    
    def get_item_dict(self):
        print(self.__dict__)
        return self.__dict__