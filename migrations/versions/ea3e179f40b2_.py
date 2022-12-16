"""empty message

Revision ID: ea3e179f40b2
Revises: b97226422ccc
Create Date: 2022-11-28 21:04:51.537506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3e179f40b2'
down_revision = 'b97226422ccc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('client_ip', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('client_user_agent', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client_info', schema=None) as batch_op:
        batch_op.drop_column('client_user_agent')
        batch_op.drop_column('client_ip')

    # ### end Alembic commands ###