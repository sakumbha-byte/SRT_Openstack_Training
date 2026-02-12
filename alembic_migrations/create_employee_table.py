from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employee',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('name', sa.String(256), nullable=False),
        sa.Column('gender', sa.String(8)),
        sa.Column('position', sa.String(56)),
        sa.Column('salary', sa.Float),
        sa.Column('experience', sa.Integer),
        sa.Column('birth_date', sa.Date),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('deleted_at', sa.DateTime),
        sa.Column('deleted', sa.Boolean, default=False)
    )


def downgrade():
    op.drop_table('employee')
