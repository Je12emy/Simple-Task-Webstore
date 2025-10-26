from flask import Flask, render_template, request
from models import Item, Category, get_items, get_categories
from database import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/store.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    category_id = request.args.get('category', type=int)
    max_price = request.args.get('max_price', type=float)
    items = get_items(category_id=category_id, max_price=max_price)
    categories = get_categories()
    return render_template('index.html', items=items, categories=categories)

@app.route('/item/<int:item_id>')
def item(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('item.html', item=item)

@app.route('/about')
def about():
    with open('content/about.md', 'r') as f:
        content = f.read()
    import markdown
    html_content = markdown.markdown(content)
    return render_template('about.html', content=html_content)

@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)