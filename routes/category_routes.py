# routes/category_routes.py

from flask import Blueprint
from handlers.post_category_handler import post_category
from handlers.get_all_categories_handler import get_all_categories

category_bp = Blueprint("category", __name__)

category_bp.route("/categories", methods=["POST"])(post_category)
category_bp.route("/categories", methods=["GET"])(get_all_categories)