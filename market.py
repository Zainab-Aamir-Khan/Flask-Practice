from flask import Flask
app =  Flask(__name__)

@app.route('/') #decorator
def hello_world():
    return "<h1>hello people from sana Aamir Khan!!</h1>"
