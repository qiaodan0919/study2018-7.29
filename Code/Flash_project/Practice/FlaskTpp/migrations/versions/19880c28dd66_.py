"""empty message

Revision ID: 19880c28dd66
Revises: 
Create Date: 2018-10-22 20:10:53.247775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19880c28dd66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_user')
    # ### end Alembic commands ###