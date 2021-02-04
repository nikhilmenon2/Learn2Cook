from flask import Blueprint, jsonify, request
from app.models import db, Recipe, Review, User, Ingredient, Instruction
import json

recipes_routes = Blueprint('recipes', __name__)


@recipes_routes.route('/<int:recipeId>')
def recipe(recipeId):
    recipedata = Recipe.query.filter(Recipe.id == recipeId).one()
    reviewsdata = Review.query.filter(Review.recipeId == recipeId).all()
    ingredientsdata = Review.query.filter(
        Ingredient.recipeId == recipeId).all()
    instructiondata = Review.query.filter(
        Instruction.recipeId == recipeId).all()

    recipe = recipedata.to_dict()
    review = [review.to_dict() for review in reviewsdata]
    ingredients = [ingredients.to_dict() for ingredients in ingredientsdata]
    instructions = [instruction.to_dict() for instruction in instructiondata]

    return jsonify("recipedata", {
        "recipe": recipe,
        "review": review,
        "ingredients": ingredients,
        "instructions": instructions


    })
