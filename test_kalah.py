from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6,4)

    def test_init_status(self):
       assert self.game.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)

    def test_init_play(self):
        assert self.game.play(1) == "Player 2 plays next"
        assert self.game.play(1) == "Player 1 plays next"
        self.assertRaises(ValueError, self.game.play, -2)
        self.assertRaises(ValueError, self.game.play, 7)
        self.assertRaises(ValueError, self.game.play, self.game.holes)

    def test_init_done(self):
        assert self.game.game_over == False

    def test_init_score(self):
        assert self.game.score() == (0,0)

    def test_simple_move(self):
        self.game.play(2)
        assert self.game.status() == (4,4,0,5,5,5,1,4,4,4,4,4,4,0)

    def test_few_moves(self):

        self.game.play(2)
        assert self.game.status() == (4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0)

        self.game.play(3)
        assert self.game.status() == (4, 4, 0, 0, 6, 6, 2, 5, 5, 4, 4, 4, 4, 0)

        self.game.play(4)
        assert self.game.status() == (5, 5, 0, 0, 6, 6, 2, 5, 5, 4, 4, 0, 5, 1)

        self.game.play(0)
        assert self.game.status() == (0, 6, 1, 1, 7, 7, 2, 5, 5, 4, 4, 0, 5, 1)

        self.assertRaises(ValueError, self.game.play, 4)

        self.game.play(0)
        assert self.game.status() == (0, 6, 1, 1, 7, 7, 2, 0, 6, 5, 5, 1, 6, 1)

    def test_captures(self):

        self.game.set_board([0, 0, 4, 4, 4, 9, 5, 5, 5, 4, 4, 4])
        self.game.play(5)
        assert self.game.status() == (1, 0, 4, 4, 4, 0, 7, 6, 6, 6, 5, 0, 5, 0)

        self.game.set_board([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 8])
        self.game.play(5)
        assert self.game.status() == (5, 5, 5, 5, 5, 0, 7, 0, 4, 4, 4, 4, 0, 7)

        self.game.set_board([1, 0, 4, 5, 4, 5, 7, 7, 6, 6, 0, 3])
        self.game.set_bank([0,0])
        self.game.play(0)
        assert self.game.status() == (0, 1, 4, 5, 4, 5, 0, 7, 7, 6, 6, 0, 3, 0)


    def test_f_play_win(self):

        self.game.set_board([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])
        self.game.set_bank([5,1])
        assert self.game.play(5) == "Player 1 wins"

    def test_s_play_win(self):

        self.game.set_board([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.game.set_bank([0,0])
        self.game.play(1)
        assert self.game.play(5) == "Player 2 wins"

    def test_tie(self):
        self.game.set_board([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.game.set_bank([2, 0])
        self.game.play(1)
        assert self.game.play(5) == "Tie"

    def test_repr(self):
        assert repr(Kalah(6,4)) == "Kalah(4, 6, status=(4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0), player=0)"


if __name__ == '__main__':
    unittest.main()
