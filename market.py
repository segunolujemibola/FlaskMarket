from unittest import TextTestRunner
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"{self.name}"

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/market')
def market_page():
    items =Item.query.all()
    col_names = Item.query.statement.columns.keys()

    return render_template('market.html', items=items,col_names=col_names)


if __name__ == '__main__':
    app.run(debug=True)
