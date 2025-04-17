from http import HTTPStatus

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from learn_fastapi.routers import auth, me, users
from learn_fastapi.schemas.message import MessageSchema
from learn_fastapi.schemas.pet import (
    CreatePetSchema,
    GetPetSchema,
    GetPetWithOwnersSchema,
    GetPetsSchema
)

app = FastAPI(version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(me.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def get_root():
    return {'message': 'Olá @lucasschilin, olá Mundo! 🌎'}
