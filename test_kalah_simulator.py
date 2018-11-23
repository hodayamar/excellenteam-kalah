import unittest

import kalah_simulator
class KalahSimulatorTestCase(unittest.TestCase):
    def setUp(self):
        with open(f"data/game_2.txt") as f:
            self.lines_first_game = f.read().splitlines()
        with open(f"data/game_3.txt") as f:
            self.lines_second_game = f.read().splitlines()


    def  test_first_game(self):
        steps = kalah_simulator.parse_game(self.lines_first_game)
        for message, status in kalah_simulator.simulate_game(6, 6, steps).items():
            self.assertEqual((0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 0, 34), status)
            self.assertEqual(message, "Player 1 wins")

    def test_second_game(self):
        steps = kalah_simulator.parse_game(self.lines_second_game)

        for message, status in kalah_simulator.simulate_game(6, 6, steps).items():
            self.assertEqual((0, 0, 0, 0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 25), status)
            self.assertEqual(message, "Player 1 wins")



if __name__ == '__main__':
    unittest.main()
