"""Primera database 1

Revision ID: a79ae43e95e7
Revises: 
Create Date: 2022-10-06 16:46:11.743044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a79ae43e95e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carrera',
    sa.Column('CarreraID', sa.Integer(), nullable=False),
    sa.Column('CarreraNombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('CarreraID')
    )
    op.create_table('orientacion',
    sa.Column('OrientacionID', sa.Integer(), nullable=False),
    sa.Column('OrientacionNombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('OrientacionID')
    )
    op.create_table('plan',
    sa.Column('PlanID', sa.Integer(), nullable=False),
    sa.Column('PlanNombre', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('PlanID')
    )
    op.create_table('carpo',
    sa.Column('CarpoID', sa.Integer(), nullable=False),
    sa.Column('CarreraID', sa.Integer(), nullable=False),
    sa.Column('PlanDeEstudioID', sa.Integer(), nullable=False),
    sa.Column('OrientacionID', sa.Integer(), nullable=True),
    sa.Column('CarpoPrograma', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['CarreraID'], ['carrera.CarreraID'], ),
    sa.ForeignKeyConstraint(['OrientacionID'], ['orientacion.OrientacionID'], ),
    sa.ForeignKeyConstraint(['PlanDeEstudioID'], ['plan.PlanID'], ),
    sa.PrimaryKeyConstraint('CarpoID')
    )
    op.create_table('materia',
    sa.Column('MateriaID', sa.Integer(), nullable=False),
    sa.Column('MateriaNombre', sa.String(length=255), nullable=True),
    sa.Column('MateriaAño', sa.String(length=255), nullable=True),
    sa.Column('MateriaTipo', sa.String(length=255), nullable=True),
    sa.Column('CarpoIDMat', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['CarpoIDMat'], ['carpo.CarpoID'], ),
    sa.PrimaryKeyConstraint('MateriaID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('materia')
    op.drop_table('carpo')
    op.drop_table('plan')
    op.drop_table('orientacion')
    op.drop_table('carrera')
    # ### end Alembic commands ###
