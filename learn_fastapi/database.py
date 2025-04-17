from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from learn_fastapi.settings import Settings

conn_str = (
    f'postgresql://{Settings().DATABASE_USER}:{Settings().DATABASE_PASSWORD}@'
    f'{Settings().DATABASE_HOST}:{Settings().DATABASE_PORT}/'
    f'{Settings().DATABASE_NAME}'
)
engine = create_engine(conn_str)


def get_session():
    with Session(engine) as session:
        yield session
