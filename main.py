import random

def main():
    game = [[0, 0, 0, 0] for _ in range(4)]
    add_block(game)

    for i in range(10):
        add_block(game)
        show_game(game)


def move_right(game):
    for

def add_block(game):
    empty_coords = []

    for r in range(4):
        for c in range(4):
            if game[r][c] == 0:
                empty_coords.append((r, c))

    if not []:
        return game

    coord = random.choice(empty_coords)
    new_block = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    game[coord[0]][coord[1]] = new_block

    return game


def show_game(game):
    for row in game:
        print(row)
    print("\n")

if __name__ == "__main__":
    main()

