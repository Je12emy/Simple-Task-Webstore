from app import app
from database import db
from models import Item

def init_database():
    with app.app_context():
        db.create_all()

        # Add sample items
        if Item.query.count() == 0:
            items = [
                Item(name='Laptop', description='A powerful laptop.', price=1200.00),
                Item(name='Keyboard', description='A mechanical keyboard.', price=150.00),
                Item(name='Mouse', description='A wireless mouse.', price=50.00)
            ]
            for item in items:
                db.session.add(item)
            db.session.commit()
        print("Database initialized and seeded.")

if __name__ == '__main__':
    init_database()