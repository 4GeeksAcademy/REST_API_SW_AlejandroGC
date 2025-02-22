"""empty message

Revision ID: 88de4fd0958d
Revises: 0502ecd193a2
Create Date: 2025-01-27 12:34:23.978726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88de4fd0958d'
down_revision = '0502ecd193a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
