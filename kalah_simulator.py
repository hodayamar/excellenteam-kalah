from kalah import Kalah
import itertools

def parse_game(lines):

    all_games = []

    for i in range(0, len(lines)) :
        all_games.append(' '.join(x for x in lines[i]  if x.isalpha()))
        all_games = ' '.join(all_games).split(' ')

    index = "abcdefABCDEF"

    for i in range(0, len(all_games)):
        all_games[i] = index.index(all_games[i])
    return all_games

def simulate_game(holes, seeds, steps):

    game = Kalah(holes,seeds)

    for i in range(0, len(steps)):
        if steps[i] > holes - 1:
            steps[i] -= holes
        game.play(steps[i])
    print(game.status())

def render_game(holes, seeds, steps):
    pass


if __name__ == "__main__":
    with open(f"data/game_2.txt") as f:
        lines = f.read().splitlines()

    steps = parse_game(lines)
    simulate_game(6, 6, steps)
    # print(render_game(6, 6, steps))
