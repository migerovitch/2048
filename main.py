from game import *
from train import *
from model import MyModel
from model import *
import pygame


def main():
    pygame.init()
    new_game = Game("eval")
    new_game.game_loop()

if __name__ == "__main__":
    pygame.init()
    main()
    #train()
