from moves import move


def score(grid):
    maxim = 0
    for row in grid:
        if max(row) > maxim:
            maxim = max(row)

    return maxim


def branch_out(grid, score=0, n=1):
    """
    :param grid: list 4x4, game position
    :param score:
    :param n: number of moves ahead
    :return:
    """

    games = []

    for _ in range(n):
        for k in range(3):
            games.append(move(grid, score, k))
    return games
