from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mail import Mail, Message
from models import Item, Category, get_items, get_categories, db
from sqlalchemy import func
import os

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/store.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-Mail configuration for MailHog
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_DEFAULT_SENDER'] = 'contact@webstore.com'

mail = Mail(app)
db.init_app(app)

@app.route('/')
def index():
    sort_by = request.args.get('sort_by', 'name')
    category_id = request.args.get('category', type=int)
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    cursor = request.args.get('cursor', type=int)
    
    per_page = 9
    items = get_items(
        sort_by=sort_by,
        category_id=category_id,
        min_price=min_price,
        max_price=max_price,
        cursor=cursor,
        per_page=per_page
    )

    next_cursor = items[-1].id if len(items) == per_page else None
    
    categories = get_categories()
    max_item_price = db.session.query(func.max(Item.price)).scalar() or 10000

    favorites = session.get('favorites', [])
    return render_template('index.html', items=items, categories=categories, max_item_price=max_item_price, favorites=favorites, next_cursor=next_cursor, prev_cursor=cursor)

@app.route('/item/<int:item_id>')
def item(item_id):
    item = Item.query.get_or_404(item_id)
    favorites = session.get('favorites', [])
    return render_template('item.html', item=item, favorites=favorites)
@app.route('/item/<int:item_id>/image')
def item_image(item_id):
    item = Item.query.get_or_404(item_id)
    if item.image_data:
        return app.response_class(item.image_data, mimetype=item.image_mimetype)
    return 'No Image', 404

@app.route('/about')
def about():
    with open('content/about.md', 'r') as f:
        content = f.read()
    import markdown
    html_content = markdown.markdown(content)
    return render_template('about.html', content=html_content)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        message_body = request.form['message']

        msg = Message("New Contact Form Submission",
                      recipients=["your_email@example.com"])  # Replace with your email
        msg.body = f"""
        From: {first_name} {last_name} <{email}>
        
        {message_body}
        """
        mail.send(msg)
        
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')
@app.route('/favorites/toggle/<int:product_id>', methods=['POST'])
def toggle_favorite(product_id):
    favorites = session.get('favorites', [])
    if product_id in favorites:
        favorites.remove(product_id)
        session['favorites'] = favorites
        flash('Item removed from favorites.', 'success')
    else:
        favorites.append(product_id)
        session['favorites'] = favorites
        flash('Item added to favorites!', 'success')
    return redirect(request.referrer or url_for('index'))

@app.route('/favorites')
def favorites():
    favorite_ids = session.get('favorites', [])
    if favorite_ids:
        favorite_items = Item.query.filter(Item.id.in_(favorite_ids)).all()
    else:
        favorite_items = []
    return render_template('favorites.html', items=favorite_items)
if __name__ == '__main__':
    app.run(debug=True)