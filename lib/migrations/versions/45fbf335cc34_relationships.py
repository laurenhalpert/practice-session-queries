"""relationships

Revision ID: 45fbf335cc34
Revises: dacd00202d2f
Create Date: 2023-06-09 11:40:53.761537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45fbf335cc34'
down_revision = 'dacd00202d2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('book_id', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('reader_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reviews', 'readers', ['reader_id'], ['id'])
    op.create_foreign_key(None, 'reviews', 'books', ['book_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'reader_id')
    op.drop_column('reviews', 'book_id')
    # ### end Alembic commands ###