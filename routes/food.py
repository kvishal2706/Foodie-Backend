from flask import Blueprint
from controllers.food import add_food_item, view_food_items

food_bp = Blueprint('food', __name__)

food_bp.route('/add', methods=['POST'])(add_food_item)
food_bp.route('/view', methods=['GET'])(view_food_items)
