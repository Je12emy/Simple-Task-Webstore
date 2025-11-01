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
    image_data = db.Column(db.LargeBinary, nullable=True)  # Store image data
    image_mimetype = db.Column(db.String(50), nullable=True) # Store mimetype
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('items', lazy=True))

    def __repr__(self):
        return f'<Item {self.name}>'

def get_items(category_id=None, min_price=None, max_price=None, sort_by=None, cursor=None, per_page=9):
    query = Item.query

    if category_id is not None and category_id != '':
        query = query.filter(Item.category_id == category_id)
    if min_price is not None:
        query = query.filter(Item.price >= min_price)
    if max_price is not None:
        query = query.filter(Item.price <= max_price)
    
    if sort_by == 'price_asc':
        query = query.order_by(Item.price.asc(), Item.id.asc())
    elif sort_by == 'price_desc':
        query = query.order_by(Item.price.desc(), Item.id.asc())
    else:
        query = query.order_by(Item.name.asc(), Item.id.asc())

    if cursor is not None:
        if sort_by == 'price_asc':
            cursor_item = Item.query.get(cursor)
            if cursor_item:
                query = query.filter(
                    (Item.price > cursor_item.price) |
                    ((Item.price == cursor_item.price) & (Item.id > cursor_item.id))
                )
        elif sort_by == 'price_desc':
            cursor_item = Item.query.get(cursor)
            if cursor_item:
                query = query.filter(
                    (Item.price < cursor_item.price) |
                    ((Item.price == cursor_item.price) & (Item.id > cursor_item.id))
                )
        else: # sort_by == 'name'
            cursor_item = Item.query.get(cursor)
            if cursor_item:
                query = query.filter(
                    (Item.name > cursor_item.name) |
                    ((Item.name == cursor_item.name) & (Item.id > cursor_item.id))
                )
    
    return query.limit(per_page).all()

def get_categories():
    return Category.query.all()