"""empty message

Revision ID: 70bed5ef46b3
Revises: b55f14baf94f
Create Date: 2025-01-24 15:51:22.407518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70bed5ef46b3'
down_revision = 'b55f14baf94f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('vehicles')
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.drop_column('birth_year')
        batch_op.drop_column('description')
        batch_op.drop_column('gender')
        batch_op.drop_column('mass')
        batch_op.drop_column('created')
        batch_op.drop_column('eye_color')
        batch_op.drop_column('hair_color')
        batch_op.drop_column('height')
        batch_op.drop_column('edited')
        batch_op.drop_column('skin_color')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.Integer(), nullable=True))
        batch_op.drop_column('population')
        batch_op.drop_column('birth_year')
        batch_op.drop_column('diameter')
        batch_op.drop_column('rotation_period')
        batch_op.drop_column('surface_water')
        batch_op.drop_column('terrain')
        batch_op.drop_column('description')
        batch_op.drop_column('orbital_period')
        batch_op.drop_column('created')
        batch_op.drop_column('climate')
        batch_op.drop_column('gravity')
        batch_op.drop_column('edited')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('edited', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('gravity', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('climate', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('orbital_period', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=400), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('terrain', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('surface_water', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rotation_period', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('diameter', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('birth_year', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('population', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_column('size')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('skin_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('edited', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('height', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('hair_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('eye_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('mass', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('gender', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=400), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('birth_year', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.drop_column('age')

    op.create_table('vehicles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(length=400), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('vehicle_class', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('manufacturer', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('cost_in_credits', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('length', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('crew', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('passengers', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('max_atmosphering_speed', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('cargo_capacity', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('consumables', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('created', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('edited', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='vehicles_pkey')
    )
    op.drop_table('favourites')
    # ### end Alembic commands ###
