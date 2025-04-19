from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session

from learn_fastapi.models.pet import Pet
from learn_fastapi.models.pet_owner import PetOwner
from learn_fastapi.models.user import User
from learn_fastapi.schemas.pet import CreatePetSchema


def controller_create_pet(
    body: CreatePetSchema, session: Session, current_user: User
):
    try:
        pet = Pet(
            name=body.name,
            specie=body.specie,
            mother=body.mother,
            father=body.father,
            created_by=current_user.id,
        )
        session.add(pet)
        session.flush()

        pet_owner = PetOwner(
            pet=pet.id, owner=current_user.id, created_by=current_user.id
        )
        session.add(pet_owner)

        session.commit()

    except Exception:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='An unexpected error occurred.',
        )

    for obj in [pet, pet_owner]:
        session.refresh(obj)

    return pet
