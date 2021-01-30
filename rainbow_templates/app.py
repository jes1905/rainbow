from flask import Flask, render_template, current_app as app

app = Flask(__name__)

name = "Jade"

@app.route('/')
def index():
    return render_template('rainbow.html', name = name)

@app.route('/red')
def red():
     return render_template('rainbow.html', color="red", name = name)

@app.route('/orange')
def orange():
      return render_template('rainbow.html', color="orange",name = name)


@app.route('/yellow')
def yellow():
      return render_template('rainbow.html', color="yellow", name = name)

@app.route('/green')
def green():
      return render_template('rainbow.html', color="green", name = name)

@app.route('/blue')
def blue():
      return render_template('rainbow.html', color="blue", name = name)

@app.route('/indigo')
def indigo():
      return render_template('rainbow.html', color="indigo", name = name)

@app.route('/violet')
def violet():
      return render_template('rainbow.html', color="violet", name = name)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

