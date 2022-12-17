
from flask import Flask, render_template, request, redirect
from logic import TicTacToe
from random import randint
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        print (username)
        return redirect('/play/'+ username)
    elif request.method=='GET':
        return render_template('login.html')

@app.route('/play/<name>')
def play(name):
    return render_template('play.html', name=name)

@app.route('/stats/<name>')
def stats(name):
    return render_template('stats.html', name=name)

app.run(port=5000, debug=True)