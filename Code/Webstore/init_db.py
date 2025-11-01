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
            with open('images/laptop.jpg', 'rb') as f:
                laptop_image = f.read()
            with open('images/keyboard.jpg', 'rb') as f:
                keyboard_image = f.read()
            with open('images/mouse.jpg', 'rb') as f:
                mouse_image = f.read()

            items = [
                Item(name='Laptop', description='A powerful laptop.', price=1200.00, category=electronics, image_data=laptop_image, image_mimetype='image/jpeg'),
                Item(name='Keyboard', description='A mechanical keyboard.', price=150.00, category=accessories, image_data=keyboard_image, image_mimetype='image/jpeg'),
                Item(name='Mouse', description='A wireless mouse.', price=50.00, category=accessories, image_data=mouse_image, image_mimetype='image/jpeg')
            ]
            for item in items:
                db.session.add(item)
            db.session.commit()
        print("Database initialized and seeded.")

if __name__ == '__main__':
    init_database()