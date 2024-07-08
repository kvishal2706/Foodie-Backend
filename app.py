from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)

# Import the User, Food, and Order models to ensure they're created
from models.user import User
from models.food import Food
from models.order import Order

# Import and register blueprints
from routes.user import user_bp
from routes.food import food_bp
from routes.order import order_bp

app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(food_bp, url_prefix='/api/food')
app.register_blueprint(order_bp, url_prefix='/api/orders')

if __name__ == "__main__":
    db.create_all()  # Ensure this creates the tables in the database
    app.run(port=int(os.getenv('PORT', 8000)))
