"""empty message

Revision ID: c6ce8e11a0ff
Revises: 
Create Date: 2021-02-03 12:37:52.197087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6ce8e11a0ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('firstName', sa.String(length=50), nullable=False),
    sa.Column('lastName', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('profileImg', sa.String(length=1000), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=False),
    sa.Column('vegetarian', sa.Boolean(), nullable=False),
    sa.Column('time', sa.Integer(), nullable=False),
    sa.Column('cheap', sa.Boolean(), nullable=False),
    sa.Column('glutenfree', sa.Boolean(), nullable=False),
    sa.Column('pricePerServing', sa.Numeric(), nullable=False),
    sa.Column('servings', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=1000), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('recipeId', sa.Integer(), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], )
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('ingredientName', sa.String(length=250), nullable=False),
    sa.Column('amount', sa.Numeric(), nullable=False),
    sa.Column('unit', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instructions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('listOrder', sa.Integer(), nullable=False),
    sa.Column('specification', sa.String(length=1000), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('overall', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(length=2500), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('instructions')
    op.drop_table('ingredients')
    op.drop_table('favorites')
    op.drop_table('recipes')
    op.drop_table('users')
    # ### end Alembic commands ###
