from flask import request, jsonify
from app import db
from models.food import Food
from middlewares.auth import token_required

@token_required
def add_food_item(current_user):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    type = data.get('type')
    address = data.get('address')
    price = data.get('price')  # Ensure price field is included

    new_food = Food(name=name, description=description, type=type, address=address, price=price)
    db.session.add(new_food)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Food item added successfully', 'data': new_food.to_dict()}), 201

@token_required
def view_food_items(current_user):
    food_items = Food.query.all()
    return jsonify({'success': True, 'data': [food.to_dict() for food in food_items]}), 200
