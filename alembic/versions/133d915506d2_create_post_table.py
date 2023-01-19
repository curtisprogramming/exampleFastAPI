"""create post table

Revision ID: 133d915506d2
Revises: 
Create Date: 2023-01-18 13:12:33.652736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '133d915506d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('posts')
    pass
