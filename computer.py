from moves import move
from random import choice as choice

def manhattan(tile1, tile2):
  return abs(tile1[0] - tile2[0]) + abs(tile1[1] - tile2[1])


def find_max_tile(grid):
    maxim = 0
    coords = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] > maxim:
                maxim = grid[i][j]
                coords = (i, j)
    return maxim, coords


def evaluate_board(board):
    max_k = 0
    max_score = 0
    new_board = [[0, 0, 0, 0] for _ in range(4)]
    children = branch_out(board)
    for k in range(len(children)):
        temp_score = children[k][1]
        """
        maxim, coords = find_max_tile(board)
        
        if coords[0] == 0:
            temp_score += maxim
        """
        if temp_score > max_score:
            max_score = temp_score
            max_k = k
            new_board = children[k][0]

    if max_score == 0:
        max_k = choice([0, 1, 2, 3])

    if board == new_board:
        max_k = choice([0, 1, 2, 3])

    return max_k

    """
    for i in board:
        for j in board[i]:
            if board[i][j] != 0:
                score += some mathy thing with (maxim - board[i][j]) and manhattan(coords, (i,j))
    """



def branch_out(grid, score=0):

    games = []

    for k in range(3):
        games.append(move(grid, score, k))

    return games
