from .db import db
from .favorites import favorites
import json


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False, default='')
    title = db.Column(db.String(1000), nullable=False)
    vegetarian = db.Column(db.Boolean, default=False, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    cheap = db.Column(db.Boolean, default=False, nullable=False)
    glutenfree = db.Column(db.Boolean, default=False, nullable=False)
    pricePerServing = db.Column(db.Numeric, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(1000), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    user = db.relationship("User", back_populates="recipes")
    reviews = db.relationship("Review", back_populates="recipes")
    favoriteUsers = db.relationship(
        "User", secondary=favorites, back_populates="favoriteRecipes")

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "title": self.title,
            "vegetarian": self.vegetarian,
            "time": self.time,
            "cheap": self.cheap,
            "glutenfree": self.glutenfree,
            "pricePerServing": float(self.pricePerServing),
            "servings": self.servings,
            "image": self.image,
            "userId": self.userId
        }
