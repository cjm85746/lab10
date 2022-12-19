# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import TicTacToe
from random import randint
import pandas as pd

"""
Return:
until there is a winner or draw, the code keep shows and updates the tic-tac-toe so that two different players or one player with a bot can play the game
"""



if __name__ == '__main__':

    ttt= TicTacToe()
    g_count=0
    empty_board = [
        [None,None,None],
        [None,None,None],
        [None,None,None]
    ]

    while g_count<10:

        #let user choose the play type
        print ('Choose a player number (1,2), Single Player(1), Multi Player(2)')
        n_player = int(input())

        if n_player ==1:
            print ('You are O')
            ttt.player_type = ttt.single_player()
        else:
            print ('O play first, and X play next')

        #Play game
        while ttt.winner == None:
            print("TODO: take a turn!")
            for i in ttt.board:
                print (i)

            # if human - allow input
            if ttt.player_type[ttt.player]:
                print("input a row number (1-3)")
                a = int(input ())
                print("input a column number (1-3)")
                b=int (input())
            #if a user put the number outisde of range, the game ask the user to input again
                (a,b) = ttt.constraint(a,b)
            #if a user choose a slot that is already occupied, the game ask the user to input again
                while ttt.board[a-1][b-1]!= None:
                    print ("Choose an empty slot")
                    print ("input a row number (1-3)")
                    a= int (input())              
                    print ("input a column number (1-3)")
                    b=int (input ())
                    (a,b) = ttt.constraint(a,b)

            #bot - automatically choose a slot
            else:
                (a,b) = ttt.bot()
            # if an user choose the slot that the other user already occupied, the game require the user to pick another slot.
            #input the value in the board
            ttt.board [a-1][b-1] = ttt.player
            ttt.count +=1

            #Check if there is an winner
            if ttt.get_winner(ttt.board) != None:
                print ("The winner is", ttt.player)
                ttt.add_games(ttt.re_board,ttt.player)
                print(ttt.re_board)
                g_count=+1
                ttt.board=empty_board
                ttt.count=0
                ttt.statistics()
                print(ttt.st_board)
                break

            # if the board is full and no winner the game is draw.
            if ttt.count ==9:
                print ("Draw")
                ttt.add_games (ttt.re_board,ttt.player)
                print(ttt.re_board)
                g_count=+1
                ttt.board=empty_board
                ttt.count=0
                ttt.statistics()
                print(ttt.st_board)
                break

            #change the player
            ttt.player = ttt.other_player(ttt.player)
            print ("Now it is", ttt.player, "'s turn")

    ttt.re_board.to_csv ("record_board.csv")
    ttt.st_board.to_csv("statistics.csv")