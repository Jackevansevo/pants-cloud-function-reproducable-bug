"""Initial migration.

Revision ID: 8e32eafd0369
Revises:
Create Date: 2024-04-07 15:54:54.145667

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8e32eafd0369"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("date_of_birth", sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("user")
