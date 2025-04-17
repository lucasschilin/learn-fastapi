from datetime import datetime

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from ._registry import table_registry


@table_registry.mapped_as_dataclass
class Pet:
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    mother: Mapped[int] = mapped_column(ForeignKey('pets.id'), nullable=True)
    father: Mapped[int] = mapped_column(ForeignKey('pets.id'), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    specie: Mapped[int] = mapped_column(
        nullable=False, comment='1 = dog; 2 = cat; 3 = hamster; 4 = snake'
    )
    created_by: Mapped[int] = mapped_column(
        ForeignKey('users.id'), init=False, nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    deleted_by: Mapped[int] = mapped_column(
        ForeignKey('users.id'), init=False, nullable=True
    )
    deleted_at: Mapped[datetime] = mapped_column(init=False, nullable=True)
