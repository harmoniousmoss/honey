# handlers/post_activity_handler.py

from flask import request, jsonify
from models.activity_model import Activity
from models.category_model import Category
from libs.db import engine
from libs.llama_client import get_ai_category_recommendation
from sqlalchemy.orm import Session
import time

def post_activity():
    start_time = time.time()
    print("📥 Received POST /activities request")
    
    data = request.get_json()
    print("📦 Request JSON:", data)

    description = data.get("description")
    category_id = data.get("category_id")

    if not description or not category_id:
        print("⚠️ Missing description or category_id")
        return jsonify({"error": "description and category_id are required"}), 400

    with Session(engine) as session:
        all_categories = session.query(Category).all()
        category_names = [cat.name for cat in all_categories]
        print("📚 Category list from DB:", category_names)

        ai_recommendation = get_ai_category_recommendation(description, category_names)
        print("🤖 AI Recommendation:", ai_recommendation)

        selected_category = session.query(Category).filter_by(id=category_id).first()
        if not selected_category:
            print(f"❌ category_id {category_id} not found")
            return jsonify({"error": "Invalid category_id"}), 404
        print(f"✅ Selected category: {selected_category.name} (ID: {selected_category.id})")

        activity = Activity(description=description, category_id=category_id)
        session.add(activity)
        session.commit()
        print(f"✅ Activity saved with ID: {activity.id}")

        response = {
            "id": activity.id,
            "description": activity.description,
            "category_id": selected_category.id,
            "category_name": selected_category.name,
            "ai_recommendation": ai_recommendation,
            "created_at": activity.created_at.isoformat(),
            "updated_at": activity.updated_at.isoformat()
        }

        end_time = time.time()
        duration_sec = round(end_time - start_time, 2)
        print(f"⏱️ Total request time: {duration_sec} seconds")

        activity.response_time_seconds = duration_sec
        session.commit()

        response = {
            "id": activity.id,
            "description": activity.description,
            "category_id": selected_category.id,
            "category_name": selected_category.name,
            "ai_recommendation": ai_recommendation,
            "created_at": activity.created_at.isoformat(),
            "updated_at": activity.updated_at.isoformat(),
            "response_time_seconds": duration_sec
        }

        return jsonify(response), 201


