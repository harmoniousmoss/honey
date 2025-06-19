# routes/activity_routes.py

from flask import Blueprint
from handlers.post_activity_handler import post_activity
from handlers.get_all_activities_handler import get_all_activities

activity_bp = Blueprint("activity", __name__)
activity_bp.route("/activities", methods=["POST"])(post_activity)
activity_bp.route("/activities", methods=["GET"])(get_all_activities)
