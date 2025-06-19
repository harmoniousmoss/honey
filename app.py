# app.py

from flask import Flask
from libs.db import test_connection, init_db
from routes.category_routes import category_bp
from routes.activity_routes import activity_bp

app = Flask(__name__)

# Run connection test immediately at import
test_connection()
init_db()

app.register_blueprint(category_bp)
app.register_blueprint(activity_bp)

@app.route("/")
def home():
    return "Welcome to FlaskLlama3"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
