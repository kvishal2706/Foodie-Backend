# routes/user.py
from flask import Blueprint
from controllers.user import create_user, login_user, validate_token

user_bp = Blueprint('user', __name__)

user_bp.route('/sign-up', methods=['POST'])(create_user)
user_bp.route('/sign-in', methods=['POST'])(login_user)
user_bp.route('/validate-token', methods=['POST'])(validate_token)
