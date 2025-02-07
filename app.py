from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy
app = Flask(__name__)
db = SQLALchemy(app)

class Item(db.Model):
    name =db.Column(db.String(length = 30), nullable = False, unique = True )
    price =db.Column(db.Integer(), nullable = False)


@app.route('/')  #Decorator
@app.route('/home')
def homePage():
    return render_template('home.html')


@app.route('/market')
def marketPage():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template('market.html', items= items)

