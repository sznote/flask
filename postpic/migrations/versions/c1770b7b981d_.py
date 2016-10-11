"""empty message

Revision ID: c1770b7b981d
Revises: 5cb7ff3456e2
Create Date: 2016-10-11 15:52:34.503795

"""

# revision identifiers, used by Alembic.
revision = 'c1770b7b981d'
down_revision = '5cb7ff3456e2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('postpic', sa.Column('link', sa.String(length=300), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('postpic', 'link')
    ### end Alembic commands ###
