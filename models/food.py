from app import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)  

    def __repr__(self):
        return f'<Food {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'address': self.address,
            'price': self.price,  
        }
