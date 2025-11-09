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

            import os

            def load_image_path(path):
                try:
                    with open(path, 'rb') as f:
                        return f.read()
                except FileNotFoundError:
                    return None

            # Build images mapping dynamically from files in images/ directory.
            images = {}
            images_dir = os.path.join(os.path.dirname(__file__), 'images')
            if os.path.isdir(images_dir):
                for fname in os.listdir(images_dir):
                    lower = fname.lower()
                    if lower.endswith(('.jpg', '.jpeg', '.png')):
                        key = os.path.splitext(fname)[0]
                        images[key] = load_image_path(os.path.join(images_dir, fname))
            else:
                # Fallback to relative path
                for fname in os.listdir('images') if os.path.isdir('images') else []:
                    lower = fname.lower()
                    if lower.endswith(('.jpg', '.jpeg', '.png')):
                        key = os.path.splitext(fname)[0]
                        images[key] = load_image_path(os.path.join('images', fname))

            import re

            def normalize_key(s):
                s = s.lower()
                # replace non-alnum with underscore
                return re.sub(r'[^a-z0-9]+', '_', s).strip('_')

            def find_image_for_name(name):
                # Try normalized name, some permutations, and substring matches
                key = normalize_key(name)
                # direct match
                if key in images and images[key]:
                    return images[key]
                # try moving leading token to end (e.g., '4k_projector' <-> 'projector_4k')
                parts = key.split('_') if key else []
                if len(parts) > 1:
                    alt = '_'.join(parts[1:] + parts[:1])
                    if alt in images and images[alt]:
                        return images[alt]
                # try removing common adjectives
                stopwords = {'wireless', 'noise', 'cancelling', 'charging', 'portable', 'high', 'large', 'feature', 'certified', 'smart', 'digital', 'mechanical', '4k'}
                tokens = [t for t in parts if t not in stopwords]
                if tokens:
                    cand = '_'.join(tokens)
                    if cand in images and images[cand]:
                        return images[cand]
                # try substring matches for any token
                for t in tokens or parts:
                    for k in images:
                        if t in k and images[k]:
                            return images[k]
                # final fallback: any image containing the first token
                if parts:
                    for k in images:
                        if parts[0] in k and images[k]:
                            return images[k]
                return None

            # Map logical items to available images (fall back to None when missing)
            items = [
                Item(name='Laptop', description='A powerful laptop.', price=1200.00, category=electronics, image_data=find_image_for_name('Laptop'), image_mimetype='image/jpeg'),
                Item(name='Keyboard', description='A mechanical keyboard.', price=150.00, category=accessories, image_data=images['keyboard'], image_mimetype='image/jpeg'),
                Item(name='Mouse', description='A wireless mouse.', price=50.00, category=accessories, image_data=images['mouse'], image_mimetype='image/jpeg'),
                Item(name='Gaming PC', description='A high-performance gaming desktop.', price=2500.00, category=electronics, image_data=images['gaming_pc'], image_mimetype='image/jpeg'),
                Item(name='Webcam', description='A 1080p HD webcam.', price=80.00, category=accessories, image_data=images['webcam'], image_mimetype='image/jpeg'),
                Item(name='Monitor', description='A 27-inch 4K monitor.', price=450.00, category=electronics, image_data=images['monitor'], image_mimetype='image/jpeg'),
                Item(name='USB-C Hub', description='A versatile USB-C hub with multiple ports.', price=60.00, category=accessories, image_data=find_image_for_name('USB-C Hub'), image_mimetype='image/jpeg'),
                Item(name='Wireless Earbuds', description='Noise-cancelling wireless earbuds.', price=180.00, category=accessories, image_data=find_image_for_name('Wireless Earbuds'), image_mimetype='image/jpeg'),
                Item(name='Smartwatch', description='A feature-rich smartwatch.', price=300.00, category=electronics, image_data=find_image_for_name('Smartwatch'), image_mimetype='image/jpeg'),
                Item(name='Portable Charger', description='A high-capacity portable charger.', price=70.00, category=accessories, image_data=find_image_for_name('Portable Charger'), image_mimetype='image/jpeg'),
                # Remaining items get a best-effort assignment from available images
                Item(name='VR Headset', description='An immersive virtual reality headset.', price=400.00, category=electronics, image_data=find_image_for_name('VR Headset'), image_mimetype='image/jpeg'),
                Item(name='Bluetooth Speaker', description='A portable Bluetooth speaker with rich sound.', price=120.00, category=accessories, image_data=find_image_for_name('Bluetooth Speaker'), image_mimetype='image/jpeg'),
                Item(name='Graphics Tablet', description='A drawing tablet for digital artists.', price=200.00, category=electronics, image_data=find_image_for_name('Graphics Tablet'), image_mimetype='image/jpeg'),
                Item(name='Ergonomic Chair', description='An ergonomic office chair for comfort.', price=350.00, category=accessories, image_data=find_image_for_name('Ergonomic Chair'), image_mimetype='image/jpeg'),
                Item(name='Standing Desk', description='An adjustable standing desk.', price=500.00, category=accessories, image_data=find_image_for_name('Standing Desk'), image_mimetype='image/jpeg'),
                Item(name='External Hard Drive', description='A 2TB external hard drive.', price=100.00, category=electronics, image_data=find_image_for_name('External Hard Drive'), image_mimetype='image/jpeg'),
                Item(name='Noise-Cancelling Headphones', description='Over-ear noise-cancelling headphones.', price=250.00, category=accessories, image_data=find_image_for_name('Noise-Cancelling Headphones'), image_mimetype='image/jpeg'),
                Item(name='4K Projector', description='A home cinema 4K projector.', price=800.00, category=electronics, image_data=find_image_for_name('4K Projector'), image_mimetype='image/jpeg'),
                Item(name='Gaming Mousepad', description='A large gaming mousepad.', price=30.00, category=accessories, image_data=find_image_for_name('Gaming Mousepad'), image_mimetype='image/jpeg'),
                Item(name='Action Camera', description='A rugged action camera for adventures.', price=280.00, category=electronics, image_data=find_image_for_name('Action Camera'), image_mimetype='image/jpeg'),
                Item(name='Smart Home Hub', description='A central hub for smart home devices.', price=150.00, category=electronics, image_data=find_image_for_name('Smart Home Hub'), image_mimetype='image/jpeg'),
                Item(name='Wireless Charging Pad', description='A Qi-certified wireless charging pad.', price=40.00, category=accessories, image_data=find_image_for_name('Wireless Charging Pad'), image_mimetype='image/jpeg'),
                Item(name='E-Reader', description='A lightweight e-reader with a paper-like display.', price=130.00, category=electronics, image_data=find_image_for_name('E-Reader'), image_mimetype='image/jpeg'),
                Item(name='Fitness Tracker', description='A sleek fitness tracker.', price=90.00, category=electronics, image_data=find_image_for_name('Fitness Tracker'), image_mimetype='image/jpeg'),
                Item(name='Drone', description='A quadcopter drone with a 4K camera.', price=600.00, category=electronics, image_data=find_image_for_name('Drone'), image_mimetype='image/jpeg'),
                Item(name='Mechanical Pencil Set', description='A set of high-quality mechanical pencils.', price=25.00, category=accessories, image_data=find_image_for_name('Mechanical Pencil Set'), image_mimetype='image/jpeg'),
                Item(name='Fountain Pen', description='A classic fountain pen for smooth writing.', price=85.00, category=accessories, image_data=find_image_for_name('Fountain Pen'), image_mimetype='image/jpeg'),
                Item(name='Leather Journal', description='A premium leather-bound journal.', price=45.00, category=accessories, image_data=find_image_for_name('Leather Journal'), image_mimetype='image/jpeg'),
                Item(name='Desk Lamp', description='An adjustable LED desk lamp.', price=55.00, category=accessories, image_data=find_image_for_name('Desk Lamp'), image_mimetype='image/jpeg'),
                Item(name='Cable Management Box', description='A box to organize and hide cables.', price=20.00, category=accessories, image_data=find_image_for_name('Cable Management Box'), image_mimetype='image/jpeg'),
                Item(name='Laptop Stand', description='An ergonomic laptop stand.', price=35.00, category=accessories, image_data=find_image_for_name('Laptop Stand'), image_mimetype='image/jpeg'),
                Item(name='Monitor Stand', description='A stand to raise your monitor to eye level.', price=40.00, category=accessories, image_data=find_image_for_name('Monitor Stand'), image_mimetype='image/jpeg'),
                Item(name='Headphone Stand', description='A stand to store your headphones.', price=25.00, category=accessories, image_data=find_image_for_name('Headphone Stand'), image_mimetype='image/jpeg'),
                Item(name='Smart Thermostat', description='A Wi-Fi enabled smart thermostat.', price=180.00, category=electronics, image_data=find_image_for_name('Smart Thermostat'), image_mimetype='image/jpeg'),
                Item(name='Smart Lock', description='A keyless smart lock for your home.', price=220.00, category=electronics, image_data=find_image_for_name('Smart Lock'), image_mimetype='image/jpeg'),
                Item(name='Robot Vacuum', description='An autonomous robot vacuum cleaner.', price=350.00, category=electronics, image_data=find_image_for_name('Robot Vacuum'), image_mimetype='image/jpeg'),
                Item(name='Air Purifier', description='A smart air purifier for clean air.', price=200.00, category=electronics, image_data=find_image_for_name('Air Purifier'), image_mimetype='image/jpeg'),
                Item(name='Electric Kettle', description='A fast-boiling electric kettle.', price=60.00, category=electronics, image_data=find_image_for_name('Electric Kettle'), image_mimetype='image/jpeg'),
                Item(name='Coffee Grinder', description='A burr coffee grinder for the perfect cup.', price=90.00, category=accessories, image_data=find_image_for_name('Coffee Grinder'), image_mimetype='image/jpeg'),
                Item(name='Espresso Machine', description='A semi-automatic espresso machine.', price=400.00, category=electronics, image_data=find_image_for_name('Espresso Machine'), image_mimetype='image/jpeg'),
                Item(name='Blender', description='A high-speed blender for smoothies.', price=150.00, category=electronics, image_data=find_image_for_name('Blender'), image_mimetype='image/jpeg'),
                Item(name='Toaster Oven', description='A versatile toaster oven.', price=120.00, category=electronics, image_data=find_image_for_name('Toaster Oven'), image_mimetype='image/jpeg'),
                Item(name='Air Fryer', description='A healthy way to fry your food.', price=100.00, category=electronics, image_data=find_image_for_name('Air Fryer'), image_mimetype='image/jpeg'),
                Item(name='Digital Scale', description='A precise digital kitchen scale.', price=30.00, category=accessories, image_data=find_image_for_name('Digital Scale'), image_mimetype='image/jpeg'),
                Item(name='Water Bottle', description='A stainless steel insulated water bottle.', price=25.00, category=accessories, image_data=find_image_for_name('Water Bottle'), image_mimetype='image/jpeg'),
                Item(name='Travel Mug', description='A spill-proof travel mug.', price=30.00, category=accessories, image_data=find_image_for_name('Travel Mug'), image_mimetype='image/jpeg'),
                Item(name='Backpack', description='A durable and stylish backpack.', price=80.00, category=accessories, image_data=find_image_for_name('Backpack'), image_mimetype='image/jpeg'),
                Item(name='Sunglasses', description='Polarized sunglasses for eye protection.', price=120.00, category=accessories, image_data=find_image_for_name('Sunglasses'), image_mimetype='image/jpeg'),
                Item(name='Wallet', description='A slim leather wallet.', price=50.00, category=accessories, image_data=find_image_for_name('Wallet'), image_mimetype='image/jpeg'),
                Item(name='Watch', description='A classic analog watch.', price=200.00, category=accessories, image_data=find_image_for_name('Watch'), image_mimetype='image/jpeg'),
                Item(name='Belt', description='A stylish leather belt.', price=45.00, category=accessories, image_data=find_image_for_name('Belt'), image_mimetype='image/jpeg'),
                Item(name='Desk Mat', description='A large desk mat to protect your desk.', price=30.00, category=accessories, image_data=find_image_for_name('Desk Mat'), image_mimetype='image/jpeg'),
                Item(name='Pen Holder', description='A stylish pen holder for your desk.', price=15.00, category=accessories, image_data=find_image_for_name('Pen Holder'), image_mimetype='image/jpeg')
            ]
            for item in items:
                db.session.add(item)
            db.session.commit()
        print("Database initialized and seeded.")

if __name__ == '__main__':
    init_database()