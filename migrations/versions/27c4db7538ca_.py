"""empty message

Revision ID: 27c4db7538ca
Revises: 9eb4b61d0acb
Create Date: 2016-06-26 09:23:07.894123

"""

# revision identifiers, used by Alembic.
revision = '27c4db7538ca'
down_revision = '9eb4b61d0acb'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role_invite', sa.Column('create_time', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role_invite', 'create_time')
    ### end Alembic commands ###