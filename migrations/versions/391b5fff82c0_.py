"""empty message

Revision ID: 391b5fff82c0
Revises: 
Create Date: 2020-05-26 19:19:11.679724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391b5fff82c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=25), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('display_pic', sa.String(length=100), nullable=True),
    sa.Column('date_joined', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###
