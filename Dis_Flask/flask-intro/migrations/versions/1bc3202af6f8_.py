"""empty message

Revision ID: 1bc3202af6f8
Revises: None
Create Date: 2016-09-22 15:20:45.432825

"""

# revision identifiers, used by Alembic.
revision = '1bc3202af6f8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    ### end Alembic commands ###
