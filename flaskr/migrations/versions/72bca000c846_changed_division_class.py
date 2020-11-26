"""Changed division class

Revision ID: 72bca000c846
Revises: 
Create Date: 2020-11-26 06:20:56.145939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72bca000c846'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('divisions', sa.Column('name', sa.String(), nullable=True))
    op.add_column('divisions', sa.Column('weight', sa.Integer(), nullable=True))
    op.drop_column('divisions', 'women_flyweight')
    op.drop_column('divisions', 'men_welterweight')
    op.drop_column('divisions', 'men_lightweight')
    op.drop_column('divisions', 'men_featherweight')
    op.drop_column('divisions', 'men_flyweight')
    op.drop_column('divisions', 'women_featherweight')
    op.drop_column('divisions', 'women_strawweight')
    op.drop_column('divisions', 'men_lightheavyweight')
    op.drop_column('divisions', 'women_bantamweight')
    op.drop_column('divisions', 'men_bantamweight')
    op.drop_column('divisions', 'men_middleweight')
    op.drop_column('divisions', 'men_heavyweight')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('divisions', sa.Column('men_heavyweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_middleweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_bantamweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('women_bantamweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_lightheavyweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('women_strawweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('women_featherweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_flyweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_featherweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_lightweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('men_welterweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('divisions', sa.Column('women_flyweight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('divisions', 'weight')
    op.drop_column('divisions', 'name')
    # ### end Alembic commands ###
