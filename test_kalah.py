from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def test_status(self):

       assert Kalah(6,4).status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)


if __name__ == '__main__':
    unittest.main()
