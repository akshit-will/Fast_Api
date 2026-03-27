"""add last few columns to posts table

Revision ID: ddb02ec131c3
Revises: c072882a604b
Create Date: 2026-03-27 07:56:20.983753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddb02ec131c3'
down_revision: Union[str, Sequence[str], None] = 'c072882a604b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa. Boolean(), nullable=False, server_default='TRUE' ) , )
    op.add_column('posts', sa.Column(
        'created_at', sa. TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
