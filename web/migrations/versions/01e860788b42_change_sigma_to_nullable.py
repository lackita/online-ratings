"""Change sigma to nullable

Revision ID: 01e860788b42
Revises: ad456cec28f4
Create Date: 2017-01-01 01:14:33.127605

"""

# revision identifiers, used by Alembic.
revision = '01e860788b42'
down_revision = 'ad456cec28f4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rating', 'sigma',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rating', 'sigma',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    ### end Alembic commands ###