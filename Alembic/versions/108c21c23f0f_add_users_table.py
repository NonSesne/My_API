"""Add Users Table

Revision ID: 108c21c23f0f
Revises: c6d5e92052b8
Create Date: 2024-01-05 14:18:08.641437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '108c21c23f0f'
down_revision: Union[str, None] = 'c6d5e92052b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('username',sa.String(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False,unique=True),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'))
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
