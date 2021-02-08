from flask import Blueprint, jsonify, request
from app.models import db, Recipe, Review, User, Ingredient, Instruction
import json

recipes_routes = Blueprint('recipes', __name__)


@recipes_routes.route('/<int:recipeId>')
def recipe(recipeId):
    recipedata = Recipe.query.filter(Recipe.id == recipeId).one()
    reviewsdata = Review.query.filter(Review.recipeId == recipeId).join(User, User.id == Review.userId).order_by(Review.id.desc()).all()
    ingredientsdata = Ingredient.query.filter(Ingredient.recipeId == recipeId).all()
    instructiondata = Instruction.query.filter(Instruction.recipeId == recipeId).order_by(Instruction.listOrder).all()
    authordata = User.query.get(recipedata.userId)
   
    recipe = recipedata.to_dict()
    review = [review.to_dict() for review in reviewsdata]
    ingredients = [ingredients.to_dict() for ingredients in ingredientsdata]
    instructions = [instruction.to_dict() for instruction in instructiondata]
    author = authordata.to_dict()
  

    return jsonify({
        "recipe": recipe,
        "review": review,
        "ingredients": ingredients,
        "instructions": instructions,
        "author": author,
       


    })


@recipes_routes.route('/')
def getrecipes():
    allrecipes = Recipe.query.all()
    recipes = [recipe.to_dict() for recipe in allrecipes]
    return jsonify({"allrecipes": recipes})


@recipes_routes.route('/homerecipes')
def gethomerecipe():
    vegdata = Recipe.query.filter(Recipe.vegetarian == True).all()
    recipes = [recipe.to_dict() for recipe in vegdata]
    return jsonify({"veg": recipes})
