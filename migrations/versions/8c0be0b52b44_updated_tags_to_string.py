"""Updated tags to String

Revision ID: 8c0be0b52b44
Revises: 4f1b382f29f9
Create Date: 2025-02-15 22:57:46.527183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c0be0b52b44'
down_revision = '4f1b382f29f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.alter_column('alt_text',
               existing_type=sa.TEXT(),
               type_=sa.String(length=512),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.alter_column('alt_text',
               existing_type=sa.String(length=512),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
