from flask import Flask, redirect, url_for, render_template, current_app as app
import request
from sense_hat import SenseHat
from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
     if request.method == 'POST':
         user = request.form['name']
         return redirect(url_for('login', name = user)), render_template('index.html')
     else:
         user = request.args.get('name')
         return redirect(url_for('login', name = user)), render_template('index.html')

    
@app.route('/login', methods = ['POST', 'GET'])
def login():
     



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')