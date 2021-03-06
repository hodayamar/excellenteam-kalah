class Kalah(object):

    def __init__(self, holes, seeds):

        self.board = [seeds] * holes * 2
        self.bank = [0] * 2
        self.holes = holes
        self.game_over = False
        self.current_player = 0
        self.seeds = seeds

    def status(self):

        return tuple(self.board[0: self.holes] + [self.bank[0]] + \
                     self.board[self.holes: (self.holes * 2) + 1] + [self.bank[1]])

    def set_board(self, l_board):

        self.board = l_board

    def set_bank(self, l_bank):

        self.bank = l_bank

    def if_valid_hole(self, hole):

        if hole not in range(0, self.holes):
            raise ValueError("you are not allow to do that!")

        if not self.current_player and self.board[hole] == 0 or \
                self.current_player and self.board[hole + self.holes] == 0:
            raise ValueError("This hole does not have seeds")

    def win(self):

        if self.bank[0] == self.bank[1]:
            return "Tie"

        msg = "Player 2 wins" if self.bank[1] > self.bank[0] else "Player 1 wins"
        return msg

    def current_index(self, i, hole):
        return (self.current_player * self.holes + hole + 1 + i) % (len(self.board))

    def add_seeds(self, bank, left_seeds, index):

        if left_seeds:
            if bank:
                self.bank[index] += 1
            else:
                self.board[index] += 1

    def in_right_range(self, last_index):
        return 0 <= last_index < self.holes if not self.current_player \
            else self.holes <= last_index < self.holes * 2

    def play(self, hole):

        last_index = 0
        self.if_valid_hole(hole)
        rob = True
        bonus_game = False

        hole_for_playing = hole + self.current_player * self.holes

        sum_of_seeds = self.board[hole_for_playing]
        self.board[hole_for_playing] = 0

        left_seeds = sum_of_seeds

        for i in range(0, sum_of_seeds):

            index = self.current_index(i, hole)
            if left_seeds == 1:
                last_index = index

            if not self.current_player and index == self.holes:
                if left_seeds == 1:

                    rob = False
                    bonus_game = True

                self.add_seeds(1, left_seeds, 0)
                if left_seeds:
                    left_seeds -= 1

            elif self.current_player and index == 0:
                if left_seeds == 1:
                    rob = False
                    bonus_game = True

                self.add_seeds(1, left_seeds, 1)
                if left_seeds:
                    left_seeds -= 1

            self.add_seeds(0, left_seeds, index)
            if left_seeds:
                left_seeds -= 1

        oposite_index = self.holes * 2 - 1 - last_index
        in_range = self.in_right_range(last_index)

        if self.board[last_index] == 1 and self.board[oposite_index] != 0 and rob and in_range:
            robbery = self.board[oposite_index] + self.board[last_index]
            self.board[oposite_index] = 0
            self.board[last_index] = 0
            self.bank[self.current_player] += robbery
            bonus_game = False

        if not bonus_game:
            self.current_player = not self.current_player

        f_index = (self.current_player) * self.holes
        s_index = self.holes * ((self.current_player) + 1) - 1

        if sum(self.board[f_index: s_index + 1]) == 0:
            self.bank[not self.current_player] += sum(self.board)
            self.board = [0] * self.holes * 2
            self.game_over = True

        if self.game_over:
            win = self.win()
            return win

        return f"Player {self.current_player + 1} plays next"

    def done(self):

        return self.game_over

    def score(self):

        return (self.bank[0], self.bank[1])

    def __repr__(self):
        return f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={self.current_player})"

    def render(self):

        str_status = self.status()

        board = "-------" * (self.holes + 6) + "\n"
        board += " *******   " * (self.holes + 2) + "\n" + " *     *   "

        i = self.holes * 2 - 1
        while i >= self.holes:
            board += f" *  {str_status[i + 1]}  *   "
            i -= 1
        board += f" *     *   "

        board += "\n" + f" *     *   " + f" *******   " * (self.holes) + " *     * \
          \n" + f" * {self.bank[1]}  *    " + " " * len("*******") * self.holes + "    " * self.holes  + f"* {self.bank[0]}  *\n *     *   "

        board += " *******   " * self.holes + " *     *\n *     *   "

        for i in range(0, self.holes):
            board += f" *  {str_status[i]}  *   "
        board += f" *     *   \n" + f" *******   " * (self.holes + 2)

        board += "\n" + "-------" * (self.holes + 6) + "\n"

        return board

    def __str__(self):
        return self.render()


