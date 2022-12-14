"""Added label model

Revision ID: f277f3435034
Revises: f131f37f26e8
Create Date: 2022-07-25 18:49:57.916598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f277f3435034'
down_revision = 'f131f37f26e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content', 'user_id', name='uk_content_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('label')
    # ### end Alembic commands ###
