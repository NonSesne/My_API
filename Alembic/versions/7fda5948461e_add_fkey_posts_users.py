"""Add Fkey posts-users

Revision ID: 7fda5948461e
Revises: 108c21c23f0f
Create Date: 2024-01-05 21:52:54.501415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fda5948461e'
down_revision: Union[str, None] = '108c21c23f0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post->user Fkey",source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post->user Fkey',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
