"""empty message

Revision ID: 8565f9b0b639
Revises: ceda533631c5
Create Date: 2018-10-18 15:16:39.897710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8565f9b0b639'
down_revision = 'ceda533631c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('s_phone', sa.String(length=32), nullable=True))
    op.create_unique_constraint(None, 'student', ['s_phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_column('student', 's_phone')
    # ### end Alembic commands ###
