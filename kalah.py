class Kalah(object):

    def __init__(self, holes, seeds):

        self.board = [seeds] * holes * 2
        self.bank = [0] * 2
        self.holes = holes
        self.game_over = False
        self.current_player = 0


    def status(self):

        return tuple(self.board[0 : self.holes] + [self.bank[0]] +\
                     self.board[self.holes : (self.holes * 2) + 1] + [self.bank[1]])

    def set_status(self, l_board):

        self.board = l_board

    def set_bank(self, l_bank):

        self.bank = l_bank


    def valid_hole(self,hole):

        if hole not in range(0, self.holes):
            raise ValueError("you are not allow to do that!")

        if  not self.current_player and self.board[hole] == 0 or \
                 self.current_player and self.board[hole + self.holes] == 0:
            raise ValueError("This hole does not have seeds")

    def win(self):

        if self.bank[0] == self.bank[1]:
            return "Tie"
        msg = "Player 2 wins" if self.bank[1] > self.bank[0] else "Player 1 wins"
        return msg


    def current_idex(self,i,hole):
        return (self.current_player * self.holes + hole + 1 + i) % (len(self.board))

    def add_seeds(self, bank,left_seeds,index):

        if left_seeds:
            if bank:

                self.bank[index] += 1
            else:
                self.board[index] += 1

    def play(self, hole):

        self.valid_hole(hole)

        sum_of_seeds = self.board[hole + self.current_player * self.holes]
        self.board[hole + self.current_player * self.holes] = 0

        index = 0
        left_seeds = sum_of_seeds

        for i in range(0, sum_of_seeds):
            index = self.current_idex(i, hole)
            if not self.current_player and index == self.holes:
                self.add_seeds(1, left_seeds, 0)
                left_seeds -= 1

            elif self.current_player and index == 0:
                self.add_seeds(1, left_seeds, 1)
                left_seeds -= 1

            self.add_seeds(0, left_seeds, index)
            left_seeds -= 1

        last_index = index + left_seeds
        opposite_index = self.holes * 2 -1 - last_index
        if self.board[last_index] == 1 and self.board[opposite_index] != 0:
            robbery = self.board[opposite_index] + self.board[last_index]
            self.board[opposite_index] = 0
            self.board[last_index] = 0
            self.bank[self.current_player] += robbery


        if index != self.holes and index != 0:
            self.current_player = not self.current_player


        f_index = (self.current_player) * self.holes
        s_index = self.holes * ((self.current_player) + 1) -1

        # print(f"first loc: {f_index}")
        # print(f"second loc: {s_index}")

        if sum(self.board[f_index : s_index +1]) == 0:

            self.bank[self.current_player] += sum(self.board)
            self.game_over = True

        if self.game_over:
            win = self.win()
            return win


        return  f"Player {self.current_player + 1} plays next"

    def done(self):

        return self.game_over

    def score(self):
        return (self.bank[0],self.bank[1])

# game = Kalah(6,4)
#
# game.set_status([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# game.set_bank([0,0])
# print(game.status())
#
# game.play(2)
# print(game.status())
