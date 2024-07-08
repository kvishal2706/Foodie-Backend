from flask import request, jsonify
from app import db
from models.order import Order
from models.food import Food
from middlewares.auth import token_required

@token_required
def create_order(current_user):
    data = request.get_json()
    food_item_ids = data.get('food_item_ids', [])  # Ensure this is a list of food item IDs

    # Ensure all food items exist
    food_items = Food.query.filter(Food.id.in_(food_item_ids)).all()
    if len(food_items) != len(food_item_ids):
        return jsonify({'success': False, 'message': 'One or more food items do not exist'}), 400

    new_order = Order(user_id=current_user.id)
    new_order.foods.extend(food_items)  # Use 'foods' which is the relationship attribute
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Order created successfully', 'data': new_order.to_dict()}), 201

@token_required
def view_user_orders(current_user):
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return jsonify({'success': True, 'data': [order.to_dict() for order in orders]}), 200
