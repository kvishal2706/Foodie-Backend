from flask import Blueprint
from controllers.order import create_order, view_user_orders

order_bp = Blueprint('order', __name__)

order_bp.route('/create', methods=['POST'])(create_order)
order_bp.route('/view', methods=['GET'])(view_user_orders)
