"""Refactor agent memory

Revision ID: 5987401b40ae
Revises: 1c8880d671ee
Create Date: 2024-11-25 14:35:00.896507

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5987401b40ae"
down_revision: Union[str, None] = "1c8880d671ee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("agents", "tools", new_column_name="tool_names")
    op.drop_column("agents", "memory")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("agents", "tool_names", new_column_name="tools")
    op.add_column("agents", sa.Column("memory", postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
