from moves import *
import pygame
from model import *
import numpy as np
import time
from computer import *
import random


class Game:
    def __init__(self, player="human"):
        self.player = "human"
        self.grid = [[0, 0, 0, 0] for _ in range(4)]
        self.grid = add_block(add_block(self.grid))
        self.score = 0

        self.screen = pygame.display.set_mode((800, 300))
        self.font_normal = pygame.font.Font(None, 30)
        self.font_large = pygame.font.Font(None, 50)
        self.BLACK = (10, 10, 10)

    def game_loop(self, player):
        while not is_game_over(self.grid):

            background = pygame.Surface(self.screen.get_size())
            background = background.convert()
            background.fill((250, 250, 250))

            for col in range(4):
                for row in range(4):
                    value = str(self.grid[col][row])
                    if value == "0":
                        value = " "
                    text = self.font_normal.render(value, 1, self.BLACK)
                    background.blit(text, (100+60*row, 20+60*col))

            board = pygame.draw.rect(background, self.BLACK, (80, 0, 250, 250), 2)
            rect = pygame.draw.rect(background, (0, 0, 0), (500, 60, 260, 50), 2)
            background.blit(self.font_large.render("Score: " + str(self.score), 1, self.BLACK), (510, 70))
            pygame.display.update()

            # Blit everything to the screen
            self.screen.blit(background, (0, 0))
            pygame.display.flip()

            if player == "human":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.grid, self.score = move(self.grid, self.score, 0)
                        if event.key == pygame.K_DOWN:
                            self.grid, self.score = move(self.grid, self.score, 1)
                        if event.key == pygame.K_LEFT:
                            self.grid, self.score = move(self.grid, self.score, 2)
                        if event.key == pygame.K_UP:
                            self.grid, self.score = move(self.grid, self.score, 3)
            else:
                pass

        show_board(self.grid)
        print(self.score)


def simulated_game():

    grid = [[0, 0, 0, 0] for _ in range(4)]
    grid = add_block(grid)
    grid = add_block(grid)
    score = 0
    while not is_game_over(grid):
        k = random.choice([0, 1, 2, 3])
        grid, score = move(grid, score, k)
        #   grid, score = move(grid, score, evaluate_board(grid))

    return grid, score


def show_game(grid, score):

    # Initialise screen
    screen = pygame.display.set_mode((800, 300))
    font_normal = pygame.font.Font(None, 30)
    BLACK = (10, 10, 10)
    font_large = pygame.font.Font(None, 50)

    while True:

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        for col in range(4):
            for row in range(4):
                value = str(grid[col][row])
                if value == "0":
                    value = " "
                text = font_normal.render(value, 1, BLACK)
                background.blit(text, (100 + 60 * row, 20 + 60 * col))

        board = pygame.draw.rect(background, BLACK, (80, 0, 250, 250), 2)
        rect = pygame.draw.rect(background, (0, 0, 0), (500, 60, 260, 50), 2)
        background.blit(font_large.render("Score: " + str(score), 1, BLACK), (510, 70))
        pygame.display.update()

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


def next_move(game, model):
    game = np.array(game)
    return model(game.reshape(16))
