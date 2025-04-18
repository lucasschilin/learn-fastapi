from pydantic import BaseModel

from learn_fastapi.models.pet import ESpecie
from learn_fastapi.schemas.user import GetUserSchema


class CreatePetSchema(BaseModel):
    name: str
    specie: ESpecie
    mother: int | None = None
    father: int | None = None
    owner: int | None = None


class GetPetSchema(BaseModel):
    id: int
    name: str
    specie: ESpecie
    mother: int | None = None
    father: int | None = None


class GetPetWithOwnersSchema(GetPetSchema):
    owners: list[GetUserSchema]


class GetPetsSchema(BaseModel):
    pets: list[GetPetSchema]
