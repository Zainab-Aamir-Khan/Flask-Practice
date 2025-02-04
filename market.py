from flask import Flask
app =  Flask(__name__)

@app.route('/') #decorator
def hello_world():
    return "<h1>This is a home page</h1>"

@app.route('/about')
def about_page():
    return "<h1>This is an about page!!!</h1>"

@app.route('/services')
def services_page():
    return "<h1>This is a service page</h1>"

@app.route('/contact/<username>')
def contact_page(username):
    return f'<h1>This is the contact page of {username}</h1>'

@app.route('/shop/<market>')
def shop_page(market):
    return f'<h1>This is a {market} of a beauty products</h1>'

@app.route('/carts')
def cart_page(carts):
    return "this is a cart' section"
