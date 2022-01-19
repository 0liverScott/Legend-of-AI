"""empty message

Revision ID: 523eedfe4f71
Revises: d3ec0fa268af
Create Date: 2022-01-17 13:59:40.642099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '523eedfe4f71'
down_revision = 'd3ec0fa268af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')

    # ### end Alembic commands ###
