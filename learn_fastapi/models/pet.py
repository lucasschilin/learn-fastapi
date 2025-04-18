from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from ._registry import table_registry


class ESpecie(str, Enum):
    dog = 'dog'
    cat = 'cat'
    hamster = 'hamster'
    snake = 'snake'


@table_registry.mapped_as_dataclass
class Pet:
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    mother: Mapped[int] = mapped_column(ForeignKey('pets.id'), nullable=True)
    father: Mapped[int] = mapped_column(ForeignKey('pets.id'), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    specie: Mapped[ESpecie]
    created_by: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    deleted_by: Mapped[int] = mapped_column(
        ForeignKey('users.id'), init=False, nullable=True
    )
    deleted_at: Mapped[datetime] = mapped_column(init=False, nullable=True)
