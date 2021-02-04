from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import db, User, Recipe, Review

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}
