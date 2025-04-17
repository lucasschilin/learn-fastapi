from enum import IntEnum

from pydantic import BaseModel

from learn_fastapi.schemas.user import GetUserSchema


class eSpecie(IntEnum):
    DOG = 1
    CAT = 2
    HAMSTER = 3
    SNAKE = 4


class CreatePetSchema(BaseModel):
    name: str
    specie: eSpecie
    mother: int
    father: int
    tutor: int


class GetPetSchema(BaseModel):
    id: int
    mother: int
    father: int
    name: str
    specie: eSpecie


class GetPetWithOwnersSchema(GetPetSchema):
    owners: list[GetUserSchema]


class GetPetsSchema(BaseModel):
    pets: list[GetPetSchema]
