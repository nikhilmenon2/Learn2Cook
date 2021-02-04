from flask import Blueprint, jsonify, request
from app.models import db, Recipe, Review, User, Ingredient, Instruction
import json

recipes_routes = Blueprint('recipes', __name__)


@recipes_routes.route('/<int:recipeId>')
def recipe(recipeId):
    recipedata = Recipe.query.filter(Recipe.id == recipeId).one()
    reviewsdata = Review.query.filter(Review.recipeId == recipeId).order_by(Review.id.desc()).all()
    ingredientsdata = Ingredient.query.filter(Ingredient.recipeId == recipeId).all()
    instructiondata = Instruction.query.filter(Instruction.recipeId == recipeId).order_by(Instruction.listOrder).all()
    
    recipe = recipedata.to_dict()
    review = [review.to_dict() for review in reviewsdata]
    ingredients = [ingredients.to_dict() for ingredients in ingredientsdata]
    instructions = [instruction.to_dict() for instruction in instructiondata]

    return jsonify({
        "recipe": recipe,
        "review": review,
        "ingredients": ingredients,
        "instructions": instructions,


    })


# @recipes_routes.route('/create', methods=['POST'])
# def create():
#     data = request.get_json(force=True)
#     print(data)
#     newBar = Recipe(**data)
#     db.session.add(newBar)
#     db.session.commit()
#     recipeDictionary = newRecipe.to_dict()
#     return {"id": recipeDictionary["id"]}
