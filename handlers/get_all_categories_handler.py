# handlers/get_all_categories_handler.py

from flask import jsonify
from models.category_model import Category
from libs.db import engine
from sqlalchemy.orm import Session

def get_all_categories():
    with Session(engine) as session:
        categories = session.query(Category).all()
        result = [
            {
                "id": cat.id,
                "name": cat.name,
                "created_at": cat.created_at.isoformat(),
                "updated_at": cat.updated_at.isoformat()
            }
            for cat in categories
        ]
        print(f"📦 Fetched {len(result)} categories")
        return jsonify(result), 200
