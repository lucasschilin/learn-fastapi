from enum import IntEnum
from pydantic import BaseModel

from learn_fastapi.schemas.user import GetUserSchema

class eSpecies(IntEnum):
    CAT = 1
    DOG = 2
    HAMSTER = 3
    SNAKE = 4

class CreatePetSchema(BaseModel):
    name: str
    specie: eSpecies
    mother: int
    father: int
    tutor: int

class GetPetSchema(BaseModel):
    id: int
    mother: int
    father: int
    name: str
    specie: eSpecies

class GetPetWithOwnersSchema(GetPetSchema):
    owners: list[GetUserSchema]

class GetPetsSchema(BaseModel):
    pets: list[GetPetSchema]
