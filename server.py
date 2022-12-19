
from flask import Flask, render_template, request, redirect
from logic import TicTacToe as ttt
from random import randint
import pandas as pd

app = Flask(__name__)

board = {
    1:' ', 2:' ', 3:' ',
    4:' ', 5:' ', 6:' ',
    7:' ', 8:' ', 9:' '
}
player='O'

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player=='O':
        return 'X'
    else:
        return 'O'

@app.route('/', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        return redirect('/play/'+ username)
    elif request.method=='GET':
        return render_template('login.html')

def board_transfer(board):
    global mark1
    global mark2
    global mark3
    global mark4
    global mark5
    global mark6
    global mark7
    global mark8
    global mark9
    mark1=board[1]
    mark2=board[2]
    mark3=board[3]
    mark4=board[4]
    mark5=board[5]
    mark6=board[6]
    mark7=board[7]
    mark8=board[8]
    mark9=board[9]



@app.route('/play/<name>', methods=['GET','POST'])
def play(name):
    if request.method=='POST':
        #receiving data from the front-end
        pick= int(request.form['tile1'])
        board[pick]=player
        board_transfer(board)
        return render_template('play.html', name=name, player=player,mark1=mark1,mark2=mark2,mark3=mark3,mark4=mark4,mark5=mark5,mark6=mark6,mark7=mark7,mark8=mark8,mark9=mark9) 
    else:
        return render_template('play.html', name=name)

@app.route('/stats/<name>')
def stats(name):
    return render_template('stats.html', name=name)

app.run(port=5000, debug=True)