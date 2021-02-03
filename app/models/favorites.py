from .db import db

favorites = db.Table(
    "favorites",
    db.Column("recipeId", db.Integer, db.ForeignKey("recipes.id")),
    db.Column("userId", db.Integer, db.ForeignKey("users.id"))
)
