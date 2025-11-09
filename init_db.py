from app import app
from database import db
from models import Item, Category

def init_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Add sample categories
        if Category.query.count() == 0:
            categories = [
                Category(name='Electronics'),
                Category(name='Accessories')
            ]
            for category in categories:
                db.session.add(category)
            db.session.commit()

        # Add sample items
        if Item.query.count() == 0:
            electronics = Category.query.filter_by(name='Electronics').first()
            accessories = Category.query.filter_by(name='Accessories').first()
            items = [
                Item(name='Laptop', description='A powerful laptop.', price=1200.00, category=electronics),
                Item(name='Keyboard', description='A mechanical keyboard.', price=150.00, category=accessories),
                Item(name='Mouse', description='A wireless mouse.', price=50.00, category=accessories)
            ]
            for item in items:
                db.session.add(item)
            db.session.commit()
        print("Database initialized and seeded.")

if __name__ == '__main__':
    init_database()