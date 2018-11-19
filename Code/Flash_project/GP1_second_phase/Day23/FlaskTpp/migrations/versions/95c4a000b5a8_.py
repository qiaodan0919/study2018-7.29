"""empty message

Revision ID: 95c4a000b5a8
Revises: fc9a968a3da8
Create Date: 2018-10-24 11:13:26.451376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95c4a000b5a8'
down_revision = 'fc9a968a3da8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_cinema_id', sa.Integer(), nullable=True),
    sa.Column('c_movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_cinema_id'], ['cinema_user.id'], ),
    sa.ForeignKeyConstraint(['c_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_movie')
    # ### end Alembic commands ###