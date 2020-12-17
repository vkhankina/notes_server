"""Create users table

Revision ID: e086e34f88e5
Revises: 6480c9f6fccb
Create Date: 2020-12-10 12:16:27.778278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e086e34f88e5'
down_revision = '6480c9f6fccb'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id VARCHAR(255) PRIMARY KEY,
            inserted_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
            roles VARCHAR(255) ARRAY NOT NULL DEFAULT '{"user"}'
        );  
    """)
    op.execute("""
        DELETE FROM notes;
    """)
    op.execute("""
        ALTER TABLE notes
        ADD COLUMN user_id VARCHAR(255) REFERENCES users(id) ON DELETE CASCADE NOT NULL;
    """)


def downgrade():
    op.execute("""
        ALTER TABLE notes
        DROP COLUMN IF EXISTS user_id;
    """)
    op.execute("""
        DROP TABLE IF EXISTS users;
    """)
