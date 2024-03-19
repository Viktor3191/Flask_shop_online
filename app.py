from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    isActive = db.Column(db.Boolean, default=False)
    publication_date = db.Column(db.DateTime, default=datetime.now())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/new')
def new():
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
