

import unittest
import logic
from random import randint
import pandas as pd

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.ttt = logic.TicTacToe()

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(self.ttt.get_winner(board), 'X')

    def test_single_player(self):
        player = 'X'
        self.assertEqual(self.ttt.single_player(),{'O':True, 'X': False})

    def test_other_player(self):
        player = 'O'
        self.assertEqual(self.ttt.other_player(player), 'X')

    def test_constraint(self):
        a=1
        b=1
        self.assertEqual(self.ttt.constraint(a,b), (a,b))

    def test_add_games(self):
        re_board = pd.DataFrame(columns=[
            "Game ID",
            "Player 1",
            "Player 2",
            "Winner"
        ])
        player="O"
        re_board_output = re_board.loc[0] = {
                "Game ID": len(re_board) +1,
                "Player 1": 'O',
                "Player 2" : 'X',
                "Winner": 'O'
            }
        temp = self.ttt.add_games(re_board,player)
        tempwinner=temp["Winner"]
        tempoutput = re_board_output["Winner"]
        self.assertEqual(tempwinner,tempoutput)



    

if __name__ == '__main__':
    unittest.main()