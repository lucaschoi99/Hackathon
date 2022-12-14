"""added thumb

Revision ID: 9813017e737d
Revises: ca62baf92545
Create Date: 2022-07-29 23:09:41.191687

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9813017e737d'
down_revision = 'ca62baf92545'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memo', sa.Column('thumbs', sa.Integer(), nullable=True))
    op.drop_column('memo', 'liked')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memo', sa.Column('liked', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('memo', 'thumbs')
    # ### end Alembic commands ###
