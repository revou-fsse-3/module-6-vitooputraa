from typing import TypeVar
from enum import Enum
from typing import TypeVar

T= TypeVar("T", bound=Enum)

class EnumMemberService:

    def __init__(self ,enums:T ) -> None:
        self.enums=enums

    def _getMember(self)-> list[str]:
        return [member.value for member in self.enums]

    def _stringMather(self,stringOne:str, stringTwo: str) -> bool:
        stringOne=stringOne.lower()
        stringTwo=stringTwo.lower()
        if(stringOne == stringTwo ):return True
        elif(stringOne.find(stringTwo) >-1): return True
        elif(stringTwo.find(stringOne) >-1): return True
        else: return False
    
    def getMatchValue(self,name:str)-> str:
        for i in self._getMember():
            if(self._stringMather(i, name)):
                return i 
        return ""