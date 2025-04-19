from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from learn_fastapi.controllers.pet_controller import (
    controller_create_pet,
    controller_delete_pet,
    controller_get_pet,
    controller_get_pets,
)
from learn_fastapi.database import get_session
from learn_fastapi.models.user import User
from learn_fastapi.schemas.message import MessageSchema
from learn_fastapi.schemas.pet import (
    CreatePetSchema,
    GetPetSchema,
    GetPetsSchema,
    GetPetWithOwnersSchema,
)
from learn_fastapi.security import get_current_user

router = APIRouter(prefix='/pets', tags=['Pets'])

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]


@router.get('/', status_code=HTTPStatus.OK, response_model=GetPetsSchema)
def get_pets(session: T_Session, current_user: T_CurrentUser):
    return controller_get_pets(session, current_user)


@router.get(
    '/{id}/', status_code=HTTPStatus.OK, response_model=GetPetWithOwnersSchema
)
def get_pet(id: int, session: T_Session, current_user: T_CurrentUser):
    return controller_get_pet(id, session, current_user)


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=GetPetSchema,
)
def create_pet(
    body: CreatePetSchema, session: T_Session, current_user: T_CurrentUser
):
    """Através deste endpoint é possívell cadastrar um pet"""
    return controller_create_pet(body, session, current_user)


@router.delete(
    '/{id}/', status_code=HTTPStatus.OK, response_model=MessageSchema
)
def delete_pet(id: int, session: T_Session, current_user: T_CurrentUser):
    return controller_delete_pet(id, session, current_user)
