from flask import Flask, render_template, json, jsonify
from datetime import date
import os
import requests


app = Flask(__name__, static_folder="static")
json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path,'r') as raw_json:
    json_info = json.load(raw_json)

@app.route('/')
def index():
    name = 'Jade'
    friends = ['joe', 'layla', 'kathrin', 'catherine', 'akeena']
    return render_template('index.html', greeting=name, friends = friends)

@app.route('/about')
def about():
    return '<h1>About</h1><p>some other content</p>'

@app.route('/nasa')
def show_nasa_pic():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date=' + today)
    data = response.json()
    return render_template('nasa.html', data=data)

@app.route('/api/v1/albums', methods=['GET'])
def albums_json():
    albums_info = os.path.join(app.static_folder, 'data', 'albums.json')
    with open(albums_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info) 

@app.route('/api/v1/movies', methods=['GET'])
def all_movies():
    return jsonify(json_info)


@app.route('/api/v1/movies/search_title', methods=['GET'])
def search_title():




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
