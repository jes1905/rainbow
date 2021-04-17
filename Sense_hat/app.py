from flask import Flask, redirect, url_for, request, render_template, current_app as app
import requests
from sense_hat import SenseHat
from time import sleep
import sys
import sqlite3


app = Flask(__name__)
sense = SenseHat()



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=['GET', 'POST'])
def success():
    message = request.form['message']
    name = request.form['name']
    #display on sensehat
    display = message + "by," + name
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages(name, message) VALUES((?),(?))",(name,message))
    conn.commit()
    conn.close()
    sense.show_message(message + " by " + name)
    return render_template('success.html', message = message, name = name)
     
@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name':row[0], 'message':row[1]}
        messages.append(message)
    conn.close()
    return render_template('all.html', messages = messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')