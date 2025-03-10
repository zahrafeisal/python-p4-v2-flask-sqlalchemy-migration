"""rename department

Revision ID: 8ec49bd2df83
Revises: 1fc47cab5890
Create Date: 2025-03-10 15:50:57.583920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec49bd2df83'
down_revision = '1fc47cab5890'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
