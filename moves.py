import random


def move_right(game):
    change = False

    init_game = game
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

    if change:
        return add_block(game)

    else:
        return game


def move_left(game):
    change = False

    init_game = game
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

    if change:
        return add_block(game)

    else:
        return game


def move_up(game):
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

    if change:
        return add_block(game)

    else:
        return game


def move_down(game):
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

    if change:
        return add_block(game)

    else:
        return game


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