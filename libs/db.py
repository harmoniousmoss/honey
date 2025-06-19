# libs/db.py

import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")

DB_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
engine = create_engine(DB_URL)

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful.")
    except Exception as e:
        print("❌ Database connection failed:", e)

from models.category_model import Base
from models.activity_model import Activity

def init_db():
    try:
        Base.metadata.create_all(engine)
        print("✅ Tables created or verified.")
    except Exception as e:
        print("❌ Table creation failed:", e)
