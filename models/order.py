from app import db

# Define association table for many-to-many relationship between Order and Food
order_food = db.Table('order_food',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True)
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    foods = db.relationship('Food', secondary=order_food, backref=db.backref('orders', lazy='dynamic'))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'foods': [food.to_dict() for food in self.foods]
        }
