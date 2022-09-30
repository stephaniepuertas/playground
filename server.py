# Import Flask to allow us to create our app

from turtle import bgcolor
from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/play')


@app.route('/play')
def play_default_box():
    return render_template('index.html', num=3 , bgcolor="blue")

@app.route('/play/<int:num>')
def play_default_box_num(num):
    return render_template('index.html', num=num , bgcolor="blue")



@app.route('/play/<int:num>/<bgcolor>')
def play(num, bgcolor):
    return render_template('index.html',num=num, bgcolor=bgcolor)




if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)