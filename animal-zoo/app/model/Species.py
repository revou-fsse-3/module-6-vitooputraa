from enum import Enum

class Species(Enum):
    INVERTEBRATES="Invertebrates"
    AMPHIBIANS="Amphibians"
    INSECT="Insect" 
    FISH="Fish"
    BIRD="Birds"
    REPTILES="Reptiles"
    MAMMALS="Mammals"
    def __str__(self):
        return str(self.value)

