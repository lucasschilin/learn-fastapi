# TODO: rename controller to pet_controller.py

from sqlalchemy.orm import Session

from learn_fastapi.models.pet import Pet
from learn_fastapi.models.user import User
from learn_fastapi.schemas.pet import CreatePetSchema


def controller_create_pet(
    body: CreatePetSchema, session: Session, current_user: User
):
    # TODO: Add transction && insert into relacion pets_owners
    pet = Pet(
        name=body.name,
        specie=body.specie,
        mother=body.mother,
        father=body.father,
        created_by=current_user.id,     
    )

    session.add(pet)
    session.commit()
    session.refresh(pet)

    return pet

