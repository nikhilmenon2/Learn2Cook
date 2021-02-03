from .db import db


class Instruction(db.Model):
    __tablename__ = 'instructions'

    id = db.Column(db.Integer, primary_key=True)
    recipeId = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    listOrder = db.Column(db.Integer, nullable=False)
    specification = db.Column(db.String(1000), nullable=False, default='')

    def to_dict(self):
        return {
            "id": self.id,
            "recipeId": self.recipeId,
            "listOrder": self.listOrder,
            "specification": self.specification
        }
