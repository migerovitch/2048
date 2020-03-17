import random
import copy


def move_right(game, score = 0):
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

    if change:
        return add_block(game), score

    else:
        return game, score


def move_left(game, score = 0):
    change = False

    for row in range(4):
        col = 0
        combined = False
        while col < 3:
            val = game[row][col]
            c = col
            while c < 3:
                c += 1
                if game[row][c] != 0:
                    break
            new_val = game[row][c]
            if val == 0 and new_val != 0:
                game[row][col] = new_val
                game[row][c] = 0
                change = True

            elif combined or val != new_val or new_val == 0:
                col += 1
            elif new_val == val:
                game[row][col] = val * 2
                game[row][c] = 0
                col += 1
                combined = True
                change = True
                score += val * 2

    if change:
        return add_block(game), score

    else:
        return game, score


def move_up(game, score = 0):
    change = False
    for row in range(4):
        col = 0
        combined = False
        while col < 3:
            val = game[col][row]
            c = col
            while c < 3:
                c += 1
                if game[c][row] != 0:
                    break
            new_val = game[c][row]
            if val == 0 and new_val != 0:
                game[col][row] = new_val
                game[c][row] = 0
                change = True

            elif combined or val != new_val or new_val == 0:
                col += 1
            elif new_val == val:
                game[col][row] = val * 2
                game[c][row] = 0
                col += 1
                combined = True
                change = True
                score += val * 2

    if change:
        return add_block(game), score

    else:
        return game, score


def move_down(game, score = 0):
    change = False
    for row in range(4):
        col = 3
        combined = False
        while col > 0:
            val = game[col][row]
            c = col
            while c > 0:
                c -= 1
                if game[c][row] != 0:
                    break
            new_val = game[c][row]
            if val == 0 and new_val != 0:
                game[col][row] = new_val
                game[c][row] = 0
                change = True
            elif combined or val != new_val or new_val == 0:
                col -= 1
            elif new_val == val:
                game[col][row] = val * 2
                game[c][row] = 0
                col -= 1
                combined = True
                change = True
                score += val * 2

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

    left = move_left(g)[0]
    right = move_right(g)[0]
    up = move_up(g)[0]
    down = move_down(g)[0]

    if left == game and right == game and up == game and down == game:
        return True
    else:
        return False


def show_board(game):
    for i in game:
        print(i)