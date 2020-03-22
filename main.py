from game import *
import numpy as np
import pygame
from computer import *
import game
from tqdm import tqdm



def main():
    # pygame.init()
    total_score = 0
    n = 10
    for k in range(n):
        score = simulated_game()[1]
        total_score += score
    print(total_score // n)


if __name__ == "__main__":
    main()

    """
    a = [[64, 32, 4, 0], [2, 4, 16, 32], [0, 0, 0, 0], [0, 0, 2, 0]]
    show_game(a, 0)
    games = branch_out(a)
    for game in games:
        show_game(game[0], game[1])
    """