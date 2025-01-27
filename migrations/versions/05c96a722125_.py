"""empty message

Revision ID: 05c96a722125
Revises: 19b0e2bbbe4c
Create Date: 2025-01-27 15:53:56.756528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c96a722125'
down_revision = '19b0e2bbbe4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint('people_fav_id_fkey', type_='foreignkey')
        batch_op.drop_column('fav_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fav_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('people_fav_id_fkey', 'favorites', ['fav_id'], ['id'])

    # ### end Alembic commands ###
