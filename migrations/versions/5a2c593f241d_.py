"""empty message

Revision ID: 5a2c593f241d
Revises: 28f4e4505ad3
Create Date: 2025-01-24 16:10:55.164500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2c593f241d'
down_revision = '28f4e4505ad3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favourites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('people_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planets_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'planets', ['planets_id'], ['id'])
        batch_op.create_foreign_key(None, 'people', ['people_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=20), nullable=False))
        batch_op.drop_column('is_active')
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_column('username')

    with op.batch_alter_table('favourites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planets_id')
        batch_op.drop_column('people_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
