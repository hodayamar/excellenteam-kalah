class Kalah(object):

    def __init__(self, holes, seeds):


        self.board = [seeds] * holes * 2
        self.bank = [0,0]
        self.holes = holes
        self.game_over = False
        self.current_player = 0


    def status(self):

        return tuple(self.board[0 : self.holes] + [self.bank[0]] +\
                     self.board[self.holes : (self.holes * 2) + 1] + [self.bank[1]])

    def valid_hole(self,hole):

        if hole not in range(1, self.holes):
            raise ValueError("you are not allow to do that!")

        if  not self.current_player and self.board[hole] == 0 or \
                 self.current_player and self.board[hole + self.holes] == 0:
            raise ValueError("This hole does not have seeds")

    def if_win(self, hole):

        if self.game_over:
            if self.bank[0] == self.bank[1]:
                return "tie"
            else:
                massege = "Player 1 wins" if self.bank[1] > self.bank[0] else "Player 2 wins"
                return massege


    def play(self, hole):

        self.valid_hole(hole)

        self.if_win(hole)

        self.current_player = not self.current_player
        return f"Player {self.current_player + 1} plays next"



    def done(self):

        return self.game_over

    def score(self):
        return (self.bank[0],self.bank[1])





