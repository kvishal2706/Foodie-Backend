# controllers/user.py
from flask import request, jsonify
from app import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os

def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    user_exists = User.query.filter_by(email=email).first()
    if user_exists:
        return jsonify({'success': False, 'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    token = jwt.encode({'user': email, 'role': 'user'}, os.getenv('SECRET_KEY'), algorithm='HS256')
    return jsonify({'success': True, 'message': 'User created successfully', 'data': new_user.to_dict(), 'access_token': token}), 201

def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Please fill in all fields'}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'success': False, 'message': 'User does not exist'}), 400

    if not check_password_hash(user.password, password):
        return jsonify({'success': False, 'message': 'Invalid password'}), 400

    token = jwt.encode({'user': email, 'role': user.role}, os.getenv('SECRET_KEY'), algorithm='HS256')
    return jsonify({'success': True, 'message': 'User logged in successfully', 'data': user.to_dict(), 'access_token': token}), 200

def validate_token():
    data = request.get_json()
    access_token = data.get('access_token')

    if not access_token:
        return jsonify({'success': False, 'message': 'No Access Token Found'}), 400

    try:
        decoded = jwt.decode(access_token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
        user = User.query.filter_by(email=decoded['user']).first()
        if not user:
            return jsonify({'success': False, 'message': 'User not found'}), 404

        return jsonify({'success': True, 'message': 'User validated successfully', 'data': user.to_dict(), 'access_token': access_token}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'success': False, 'message': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'success': False, 'message': 'Invalid token'}), 401
