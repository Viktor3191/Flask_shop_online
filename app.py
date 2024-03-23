from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cloudipsp import Api, Checkout


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    # quantity = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    # image = db.Column(db.LargeBinary, nullable=False)
    # publication_date = db.Column(db.DateTime, default=datetime.now())

    # text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        # quantity =request.form['quantity']
        item = Item(title=title, price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Произошла ошибка'
    else:
        return render_template('create.html')


@app.route('/buy/<int:id>')
def item_buy(id):
    item = Item.query.get(id)
    api = Api(merchant_id=1396424, secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": 1000  # item.price
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@app.route('/new')
def new():
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
