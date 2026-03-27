"""add content column to posts table

Revision ID: 3cd21ef61d5d
Revises: 605411eb90ee
Create Date: 2026-03-26 13:50:30.125389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cd21ef61d5d'
down_revision: Union[str, Sequence[str], None] = '605411eb90ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
  op.drop_column('posts', 'content')
  pass
