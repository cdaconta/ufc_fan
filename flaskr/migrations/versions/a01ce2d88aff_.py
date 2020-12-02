"""empty message

Revision ID: a01ce2d88aff
Revises: 72bca000c846
Create Date: 2020-12-01 21:42:22.173522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a01ce2d88aff'
down_revision = '72bca000c846'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fighters_division_fkey', 'fighters', type_='foreignkey')
    op.create_foreign_key(None, 'fighters', 'divisions', ['division'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fighters', type_='foreignkey')
    op.create_foreign_key('fighters_division_fkey', 'fighters', 'fighters', ['division'], ['id'])
    # ### end Alembic commands ###
