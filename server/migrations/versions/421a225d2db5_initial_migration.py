"""initial migration

Revision ID: 421a225d2db5
Revises: 
Create Date: 2024-11-27 18:03:01.058912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '421a225d2db5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###