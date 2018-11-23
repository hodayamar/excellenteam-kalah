from kalah import Kalah


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
        msg = game.play(steps[i])
    status = game.status()
    l = {msg: status}
    return l

def render_game(holes, seeds, steps):
    game = Kalah(holes, seeds)

    for i in range(0, len(steps)):
        if steps[i] > holes - 1:
            steps[i] -= holes
        print(game.play(steps[i]))
        print(game)


