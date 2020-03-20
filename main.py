from game import *
import numpy as np
import pygame
from computer import *
import game




def main():
    game_loop()


if __name__ == "__main__":
    pygame.init()

    a = [[64, 32, 4, 0], [2, 4, 16, 32], [0, 0, 0, 0], [0, 0, 2, 0]]
    show_game(a, 0)
    games = branch_out(a)
    for game in games:
        show_game(game[0], game[1])