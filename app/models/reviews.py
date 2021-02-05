from .db import db


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    overall = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(2500), nullable=False, default="")
    recipeId = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipes = db.relationship("Recipe", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "overall": self.overall,
            "review": self.review,
            "recipeId": self.recipeId,
            "userId": self.userId,
            "user": { 
                "firstName" : self.user.firstName,
                "lastName" : self.user.lastName,
                "profileImg" : self.user.profileImg
            }
        }
