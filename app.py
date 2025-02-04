from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  #Decorator
@app.route('/home')
def homePage():
    return render_template('home.html')


@app.route('/market')
def marketPage():
    return render_template('market.html', item_name= 'Phone')
