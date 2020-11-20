"""create notes table

Revision ID: 6480c9f6fccb
Revises: 
Create Date: 2020-11-20 09:21:40.328663

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '6480c9f6fccb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            inserted_at TIMESTAMP NOT NULL DEFAULT current_timestamp
        );
    """)


def downgrade():
    op.execute("""
        DROP TABLE IF EXISTS notes;
    """)
