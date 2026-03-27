"""create posts table

Revision ID: 605411eb90ee
Revises: 
Create Date: 2026-03-26 13:22:11.069320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '605411eb90ee'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
      op.create_table('posts',sa.Column('id', sa.Integer(), nullable= False
                                        , primary_key = True), sa.Column('title', sa.String(), nullable = False))
      pass


def downgrade():
    op.drop_table('posts')
    pass
