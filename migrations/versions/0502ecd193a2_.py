"""empty message

Revision ID: 0502ecd193a2
Revises: 5a2c593f241d
Create Date: 2025-01-27 11:49:49.894190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0502ecd193a2'
down_revision = '5a2c593f241d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favourites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('people_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planets_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], name='favourites_people_id_fkey'),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], name='favourites_planets_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favourites_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favourites_pkey')
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###
