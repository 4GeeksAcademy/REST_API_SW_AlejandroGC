"""empty message

Revision ID: 093ae63a7c76
Revises: e6d5b873fc73
Create Date: 2025-01-24 15:33:50.779198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '093ae63a7c76'
down_revision = 'e6d5b873fc73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=400), nullable=True))
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))
        batch_op.drop_column('is_active')
        batch_op.drop_column('email')
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_column('name')
        batch_op.drop_column('description')

    # ### end Alembic commands ###
