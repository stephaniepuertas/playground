# Import Flask to allow us to create our app
from flask import Flask, render_template

app = Flask(__name__)

# need route and method

@app.route('/play/<int:num>/<bgcolor>')
def play(num, bgcolor):
    return render_template('index.html',num=num, bgcolor=bgcolor)  

# @app.route('/')
# def index():
    return render_template("index.html", phrase="hello", times=5)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)