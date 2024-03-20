from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # image = db.Column(db.LargeBinary, nullable=False)
    # publication_date = db.Column(db.DateTime, default=datetime.now())
    # text = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create')
def create():
    return render_template('create.html')



@app.route('/new')
def new():
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
