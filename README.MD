# 🦙 FlaskLlama3

FlaskLlama3 is a Flask-based API that enables users to submit activity descriptions and receive AI-generated category recommendations using LLaMA3 (via Ollama). Final categorization is selected manually, with the AI acting as an intelligent assistant.

## 🚀 Features

- Add & retrieve activity categories (`POST /categories`, `GET /categories`)
- Add new activities with AI-assisted category suggestions (`POST /activities`)
- Retrieve all activities with enriched category data (`GET /activities`)
- Stores response time and AI recommendation for each activity
- Uses local Ollama to run LLaMA3 for inference
- Logs every request from start to finish

## 🧱 Tech Stack

- **Backend:** Flask (Python)
- **Database:** PostgreSQL (via Docker)
- **AI Model:** LLaMA3 via Ollama
- **ORM:** SQLAlchemy
- **Config:** dotenv (.env)

## 📦 API Endpoints

### 🔹 Categories

* `POST /categories`
  Create a new category.

* `GET /categories`
  Get all categories.

### 🔹 Activities

* `POST /activities`
  Submit an activity description and selected category. AI recommends the most relevant one.

* `GET /activities`
  List all activities with category name and AI recommendation.