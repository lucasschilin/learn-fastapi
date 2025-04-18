"""Change pets.specie column type

Revision ID: 111424836db4
Revises: 36d936c3b847
Create Date: 2025-04-18 18:12:14.221202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '111424836db4'
down_revision: Union[str, None] = '36d936c3b847'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# Criação do tipo ENUM
especie_enum = postgresql.ENUM('dog', 'cat', 'hamster', 'snake', name='especie')


def upgrade() -> None:
    """Upgrade schema."""
    especie_enum.create(op.get_bind())

    op.execute("""
        ALTER TABLE pets
        ALTER COLUMN specie
        TYPE especie
        USING CASE
            WHEN specie = 1 THEN 'dog'::especie
            WHEN specie = 2 THEN 'cat'::especie
            WHEN specie = 3 THEN 'hamster'::especie
            WHEN specie = 4 THEN 'snake'::especie
        END
    """)



def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE pets
        ALTER COLUMN specie
        TYPE INTEGER
        USING CASE
            WHEN specie = 'dog' THEN 1
            WHEN specie = 'cat' THEN 2
            WHEN specie = 'hamster' THEN 3
            WHEN specie = 'snake' THEN 4
        END
    """)

    especie_enum.drop(op.get_bind())

