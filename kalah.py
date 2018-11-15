class Kalah(object):

    def __init__(self, holes, seeds):

        self.board = {0: [seeds] * holes + [0], 1: [seeds] * holes + [0]}
        self.holes = holes
        self.game_over = False
        self.current_player = 0


    def status(self):

        return tuple((self.board[0]) + (self.board[1]))

    def play(self, hole):

        if hole not in range(1, self.holes):
            raise ValueError("you are not allow to do that!")

        if self.board[self.current_player][hole] == 0:
            raise  ValueError("This hole does not have seeds")

        if self.game_over:
            bank = self.holes
            if self.board[0][bank] == self.board[0][bank]:
                return "tie"
            else:
                massege = "Player 1 wins" if self.board[0][bank] > self.board[0][bank] else "Player 2 wins"
                return massege
        else:
            self.current_player = not self.current_player
            return f"Player {self.current_player + 1} plays next"

    def done(self):

        return self.game_over

    def score(self):

        bank = self.holes
        return (self.board[0][bank]),(self.board[0][bank])

# game = Kalah(6,4)





