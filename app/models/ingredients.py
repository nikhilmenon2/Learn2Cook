from .db import db


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    recipeId = db.Column(db.Integer, db.ForeignKey(
        "recipes.id"), nullable=False)
    ingredientName = db.Column(db.String(250), nullable=False, default="")
    amount = db.Column(db.Numeric, nullable=False)
    unit = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "recipeId": self.recipeId,
            "ingredientName": self.ingredientName,
            "amount": float(self.amount),
            "unit": self.unit
        }
