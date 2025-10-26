from database import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('items', lazy=True))

    def __repr__(self):
        return f'<Item {self.name}>'

def get_items(category_id=None, max_price=None):
    query = Item.query
    if category_id:
        query = query.filter(Item.category_id == category_id)
    if max_price:
        query = query.filter(Item.price <= max_price)
    return query.all()

def get_categories():
    return Category.query.all()