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

@app.route('/contact')
def contact_page();
    return

