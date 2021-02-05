from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import db, User, Recipe, Review

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}




@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/no-auth/<int:id>')
def userNoAuth(id):
    user = User.query.get(id)
    return user.to_dict_essentials()


@user_routes.route('/<int:id>/favorites')
def userfavorites(id):
    user = User.query.get(int(id))
    recipes = user.to_dict()["favoriteRecipes"]
    return {"favorites": recipes}


@user_routes.route('/<int:userId>/favorites/<int:recipeId>/delete', methods=["DELETE"])
def delete_favorite(userId, recipeId):
    userId = int(userId)
    recipeId = int(recipeId)
    user = User.query.get(userId)
    recipe = Recipe.query.get(recipeId)
    user.favoriteRecipes.remove(recipe)
    if not recipe:
        return {'msg': 'recipe not found'}, 404
    db.session.commit()
    return {"targetId": recipeId}


@user_routes.route('/<int:userId>/favorites/<int:recipeId>/add', methods=["POST"])
def add_favorite(userId, recipeId):
    userId = int(userId)
    recipeId = int(recipeId)
    user = User.query.get(userId)
    recipe = Recipe.query.get(recipeId)
    recipeDict = recipe.to_dict()

    user.favoriteRecipes.append(recipe)
    db.session.commit()
    return {"favorite": "string", "recipe": recipeDict}


@user_routes.route('/<int:userId>/reviews/recipes/<int:recipeId>', methods=['GET'])
def getReview(userId, recipeId):
    review = Review.query.filter(Review.userId == int(
        userId)).filter(Review.recipeId == int(recipeId)).first()
    if review == None:
        return {"review": False}
    else:
        return {"review": review.to_dict()}


@user_routes.route('/<int:userId>/reviews/recipe/<int:recipeId>', methods=['POST'])
def postReview(userId, recipeId):
    if request:
        data = request.get_json()

        overall = int(data['overall']['value'])
        review = str(data['review'])
        recipeId = int(recipeId)
        userId = int(userId)

        if overall > 0 and len(review) > 0 and recipeId > 0 and userId > 0:
            review = Review(
                overall=overall,
                review=review,
                recipeId=recipeId,
                userId=userId
            )
            db.session.add(review)
            db.session.commit()
            return {"message": "received, committed"}
        else:
            return {"message": "received, rejected"}


@user_routes.route('/<int:userId>/reviews/<int:id>', methods=['DELETE'])
def deleteReview(userId, id):
    if request:
        review = Review.query.filter_by(id=id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            return {"message": "deleted"}
        else:
            return {"message": "no such review?"}

    return {"message": "request is false?"}


@user_routes.route('/<int:userId>/reviews/<int:reviewId>', methods=["PATCH"])
def updateReview(userId, reviewId):
    if request:
        review = Review.query.filter_by(id=reviewId).first()
        if review:
            data = request.get_json()

            overall = int(data['overall']['value'])
            reviewStr = str(data['review'])

            review.overall = overall
            review.review = reviewStr

            db.session.commit()
            return {"message": "updated"}
        else:
            return {"message": "no such review?"}

    return {"message": "request is false?"}
