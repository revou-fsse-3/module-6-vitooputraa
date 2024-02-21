from enum import Enum

class Role(Enum):
    BOSS="Boss"
    CARETAKER="Caretaker"
    ZOOKEEPER="Zookeeper"
    def __str__(self):
        return str(self.value)
    