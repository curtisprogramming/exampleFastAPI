"""add content column to posts table

Revision ID: fd318830c827
Revises: 133d915506d2
Create Date: 2023-01-18 13:26:10.989162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd318830c827'
down_revision = '133d915506d2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('posts', 'content')
    