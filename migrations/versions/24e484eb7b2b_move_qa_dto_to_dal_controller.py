"""move qa_dto to dal_controller

Revision ID: 24e484eb7b2b
Revises: 1a4027b852e8
Create Date: 2024-10-07 07:15:40.231982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24e484eb7b2b'
down_revision: Union[str, None] = '1a4027b852e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
