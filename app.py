from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'


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
