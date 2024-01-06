"""Create Post Table

Revision ID: c6d5e92052b8
Revises: 
Create Date: 2024-01-04 20:00:54.554221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6d5e92052b8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False),
                    sa.Column('content',sa.String(),nullable=False),
                    sa.Column('publiched',sa.BOOLEAN(),nullable=True,server_default=sa.text('true')),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('NOW()'))
                    )

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
