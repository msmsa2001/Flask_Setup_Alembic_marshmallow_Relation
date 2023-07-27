"""phone column

Revision ID: fb47e355a60d
Revises: 
Create Date: 2023-07-27 11:58:43.947827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb47e355a60d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
   op.add_column('emp', sa.Column('phone', sa.String(length=50), nullable=True)) 


def downgrade() -> None:
    op.drop_column('emp', 'phone')
