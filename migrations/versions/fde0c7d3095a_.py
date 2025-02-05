"""empty message

Revision ID: fde0c7d3095a
Revises: 0fd38416743d
Create Date: 2022-11-15 18:03:46.593702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fde0c7d3095a'
down_revision = '0fd38416743d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    op.drop_constraint('task_goal_id_fkey', 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('task_goal_id_fkey', 'task', 'goal', ['goal_id'], ['goal_id'])
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
