from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from ._registry import table_registry


@table_registry.mapped_as_dataclass
class PetOwner:
    __tablename__ = 'pets_owners'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    pet: Mapped[int] = mapped_column(ForeignKey('pets.id'))
    owner: Mapped[int] = mapped_column(ForeignKey('users.id'))
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
