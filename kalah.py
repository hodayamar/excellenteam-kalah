class Kalah(object):

    def __init__(self, holes, seeds):

        self.board = {"player_one": [seeds] * holes + [0], "player_two": [seeds] * holes + [0]}
        self.turn = False

    def status(self):

        return tuple((self.board["player_one"]) + (self.board["player_two"]))

game = Kalah(6,4)
print()
print(type(game.status()))




