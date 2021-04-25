from flask import Flask, redirect, url_for, request, render_template, current_app as app
import requests
from sense_hat import SenseHat
from time import sleep
from flask_apscheduler import APScheduler
import sys
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
sense = SenseHat()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods = ['GET', 'POST'])
def tasks():
    task = request.form['task']
    time = request.form['time']
    date = request.form['date']
    conn = sqlite3.connect('./static/data/tasks.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks(task, time, date) VALUES((?),(?),(?))",(task,time,data))
    conn.commit()
    conn.close()
    return render_template('tasks.html', task = task, time = time, date = date)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')