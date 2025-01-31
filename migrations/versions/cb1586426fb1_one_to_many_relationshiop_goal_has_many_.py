"""one to many relationshiop goal has many tasks task has one goal

Revision ID: cb1586426fb1
Revises: 7f819867fb99
Create Date: 2022-05-12 13:24:34.724267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb1586426fb1'
down_revision = '7f819867fb99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_key', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_key'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_key')
    # ### end Alembic commands ###
