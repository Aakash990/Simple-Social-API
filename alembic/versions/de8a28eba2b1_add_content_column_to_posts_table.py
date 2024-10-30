"""add content column to posts table

Revision ID: de8a28eba2b1
Revises: 695791434415
Create Date: 2024-10-30 08:53:09.695951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de8a28eba2b1'
down_revision: Union[str, None] = '695791434415'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
