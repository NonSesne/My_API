"""Adding Bio,PhoneNumber,Firstname,lastname To Users Table

Revision ID: 508edd262a5c
Revises: 67439b305b6c
Create Date: 2024-01-09 01:51:37.049876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '508edd262a5c'
down_revision: Union[str, None] = '67439b305b6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=256), nullable=True))
    op.add_column('users', sa.Column('phone_number', sa.String(length=12), nullable=True))
    op.add_column('users', sa.Column('first_name', sa.String(length=12), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=12), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
