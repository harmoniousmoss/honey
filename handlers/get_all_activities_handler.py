# handlers/get_all_activities_handler.py

from flask import jsonify
from models.activity_model import Activity
from models.category_model import Category
from libs.db import engine
from sqlalchemy.orm import Session

def get_all_activities():
    with Session(engine) as session:
        activities = session.query(Activity).all()
        result = []

        for act in activities:
            # Fetch related category name (relationship or lookup)
            category = session.query(Category).filter_by(id=act.category_id).first()
            result.append({
                "id": act.id,
                "description": act.description,
                "category_id": act.category_id,
                "category_name": category.name if category else None,
                "created_at": act.created_at.isoformat(),
                "updated_at": act.updated_at.isoformat(),
                "response_time_seconds": act.response_time_seconds
            })

        print(f"📦 Fetched {len(result)} activities")
        return jsonify(result), 200
