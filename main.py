from game import *
import numpy as np
import pygame

#from computer import *
from model import *


def main():
    pygame.init()
    new_game = Game()
    new_game.game_loop("human")



if __name__ == "__main__":
    pygame.init()

    grid = [[0,0,0,0],[4,2,0,0],[8,2,2,0],[32,16,8,4]]

    grid = np.array(grid).reshape(16)
