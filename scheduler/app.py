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

@app.route('/', methods = ["GET", "POST"])
def index():
    task = request.form['task']
    date = request.form['date']
    conn = sqlite3.connect('./static/data/tasks.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks(task, date) VALUES((?),(?))",(task,date))
    conn.commit()
    conn.close()
    return render_template('index.html', task = task, date = date)

@app.route('/tasks', methods = ['GET', 'POST'])
def tasks():
    conn = sqlite3.connect('./static/data/tasks.db')
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * from tasks")
    for row in rows:
        task = {'task':row[0], 'date':row[1]}
        tasks.append(task)
    conn.close()
    return render_template('tasks.html', tasks = tasks)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')