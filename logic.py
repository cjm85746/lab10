# sThis file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

from random import randint
import pandas as pd


class TicTacToe:

    def __init__(self):
        """
        Set up a game by initializing board, player type, Player, Winner, Count
        """
        self.board = [
            [None,None,None],
            [None,None,None],
            [None,None,None]
        ]

        self.re_board = pd.DataFrame(columns=[
            "Game ID",
            "Player 1",
            "Player 2",
            "Winner"
            ])

        self.st_board =pd.DataFrame(columns=[
            "Player",
            "Wins",
            "Loses",
            "Draws"
            ])

 
        self.player_type = {'O':True, 'X': True}
        self.player = 'O'
        self.winner=None
        self.count = 0
        self.wins_O =0
        self.loses_O =0
        self.wins_O =0
        self.loses_O =0
        self.draws =0

    def single_player(self):
        self.player_type['X'] = False
        return self.player_type

    def get_winner(self,board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        #Row winner reader
        for row in range (0,2):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0]!=None:
                return board[row][0]
        #Column winner reader
        for col in range (0,2):    
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != None:
                return board[0][col]
        #Diagonal winner reader
        if board[0][0] == board[1][1]==board[2][2] and board[0][0] != None:
            return board[0][0]
        elif board[0][2] == board [1][1]==board[2][0] and board[0][2] != None:
            return board[0][2]
        #If there is no winner, return None
        else:
            return None

    def other_player(self,player):
        """Given the character for a player, returns the other player."""
        if player=='O':
            return 'X'
        else:
            return 'O'

    def constraint (self,a,b):
        """Given the inputs from a user, it ask a user to input again until it get the number between 1-3, and return the a,b"""
        while b<1 or b>3 or a<1 or a>3:
            print ("Choose a number between 1-3")
            print("input a row number (1-3)")
            a= int (input ())
            print("input a column number (1-3)")
            b = int (input ())
        return a,b
    
    def bot (self):
        """Return the randomly chosen a,b within the 1~3 range"""
        a= int(randint (1,3))
        b = int(randint (1,3))
        while self.board[a-1][b-1]!= None:
            a= int(input())
            b=int(input())
        return a,b

    def add_games (self,re_board, player):
        if self.get_winner != None:

            re_board.loc[len(re_board)] = {
                "Game ID": len(re_board) +1,
                "Player 1": 'O',
                "Player 2" : 'X',
                "Winner": player
            }
            return re_board
        elif self.count==9:
            re_board.loc [len(re_board)]={
                "Game ID": len(re_board) +1,
                "Player 1": 'O',
                "Player 2" : 'X',
                "Winner": "Draw",
            }
            return re_board
        else:
            return re_board

    def statistics (self):
        
        self.wins_O = self.re_board[self.re_board ["Winner"]=="O"]
        self.wins_X = self.re_board[self.re_board ["Winner"]=="X"]
        self.draws = self.re_board[self.re_board["Winner"]=="Draw"]

        self.loses_O = len(self.re_board)-len(self.wins_O)-len(self.draws)
        self.loses_X = len(self.re_board)-len(self.wins_X)-len(self.draws)

        self.st_board.loc [0] ={
            "Player": "O",
            "Wins": len(self.wins_O),
            "Loses": self.loses_O,
            "Draws": len(self.draws)
        }

        self.st_board.loc [1] ={
            "Player": "X",
            "Wins": len(self.wins_X),
            "Loses": self.loses_X,
            "Draws": len(self.draws)
        }

        return self.st_board
