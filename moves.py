import random
import copy
import numpy as np


def move(game, score=0, k=0):
    """
    game (list: 4x4) – the playing grid
    score (int) – self-explanatory
    k (int) – direction
        0 --> right
        1 --> down
        2 --> left
        3 --> up
    """
    game = np.rot90(np.array(game), k)

    change = False

    for row in range(4):
        col = 3
        combined = False

        while col > 0:
            val = game[row][col]
            c = col

            while c > 0:
                c -= 1
                if game[row][c] != 0:
                    break
            new_val = game[row][c]

            if val == 0 and new_val != 0:
                game[row][col] = new_val
                game[row][c] = 0
                change = True

            elif combined or val != new_val or new_val == 0:
                col -= 1

            elif new_val == val:
                game[row][col] = val * 2
                game[row][c] = 0
                col -= 1
                combined = True
                change = True
                score += val * 2

    game = np.rot90(game, 4-k).tolist()

    if change:
        return add_block(game), score

    else:
        return game, score


def add_block(game):
    empty_coords = []

    for r in range(4):
        for c in range(4):
            if game[r][c] == 0:
                empty_coords.append((r, c))

    if not empty_coords:
        return game

    coord = random.choice(empty_coords)
    new_block = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    game[coord[0]][coord[1]] = new_block

    return game


def is_game_over(game):
    g = copy.deepcopy(game)

    right = move(g)[0]
    down = move(g, k=1)[0]
    left = move(g, k=2)[0]
    up = move(g, k=3)[0]

    if left == game and right == game and up == game and down == game:
        return True
    else:
        return False


def show_board(game):
    for i in game:
        print(i)