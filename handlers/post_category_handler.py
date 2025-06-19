# handlers/post_category_handler.py

from flask import request, jsonify
from models.category_model import Category
from libs.db import engine
from sqlalchemy.orm import Session
from datetime import datetime

def post_category():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    with Session(engine) as session:
        if session.query(Category).filter_by(name=name).first():
            return jsonify({"error": "Category already exists"}), 409

        new_category = Category(name=name)
        session.add(new_category)
        session.commit()
        print(f"✅ Category created: {new_category.name}")

        return jsonify({
            "id": new_category.id,
            "name": new_category.name,
            "created_at": new_category.created_at.isoformat(),
            "updated_at": new_category.updated_at.isoformat()
        }), 201
