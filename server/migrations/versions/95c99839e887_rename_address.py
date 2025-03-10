"""rename address

Revision ID: 95c99839e887
Revises: 8ec49bd2df83
Create Date: 2025-03-10 15:56:15.651675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95c99839e887'
down_revision = '8ec49bd2df83'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'departments',
        'address',
        new_column_name='location'
    )
    # ### end Alembic commands ###


def downgrade():
    op.alter_column(
        'departments',
        'location',
        new_column_name='address'
    )
    # ### end Alembic commands ###
