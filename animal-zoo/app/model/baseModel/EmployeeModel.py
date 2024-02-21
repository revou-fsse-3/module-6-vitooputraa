from app.util.SessionFlaskModel import SessionFlaskModel
from uuid import uuid4
from app.model.Role import Role
from app.model.Schedule import Schedule
from app.service.MemberService import EnumMemberService
from dataclasses import dataclass

db= SessionFlaskModel.getSession()

class EmployeeModel(db.Model,):
    __tablename__= "employee"
    employeeId= db.Column("employee_id",  db.String, primary_key=True)
    role= db.Column("employee_role", db.String)
    schedule= db.Column("schedule", db.String) 
    name= db.Column("name", db.String) 
    email= db.Column("email", db.String) 
    phone= db.Column("phone", db.String) 

    def __init__(self, role :str, schedule:str, name:str, email:str, phone:str ):
        self.employeeId = str(uuid4())
        self.role = EnumMemberService(Role).getMatchValue(role)
        self.schedule = EnumMemberService(Schedule).getMatchValue(schedule)
        self.name = name
        self.email = email
        self.phone = phone

    def update(self, role :str =None, schedule:str=None, name:str=None, email:str=None, phone:str=None ):
        self.role = EnumMemberService(Role).getMatchValue(role) if role !=None else self.role
        self.schedule = EnumMemberService(Schedule).getMatchValue(schedule) if schedule !=None else self.schedule
        self.name = name if name !=None else self.name
        self.email = email if email !=None else self.email
        self.phone = phone if phone !=None else self.phone

    def get_item_dict(self):
        return self.__dict__
    
    def __str__ (self):
        return f"{self.role} {self.name} {self.schedule} {self.email} {self.phone}"