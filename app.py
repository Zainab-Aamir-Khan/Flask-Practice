from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  #Decorator
@app.route('/home')
def homePage():
    return render_template('home.html')


