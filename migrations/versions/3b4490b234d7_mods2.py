"""mods2

Revision ID: 3b4490b234d7
Revises: c4d44f977c2d
Create Date: 2021-02-04 10:47:43.077456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b4490b234d7'
down_revision = 'c4d44f977c2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'category')
    # ### end Alembic commands ###
