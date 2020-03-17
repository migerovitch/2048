import random
from moves import *
import pygame


def main():
    game = [[0, 0, 0, 0] for _ in range(4)]
    game = add_block(game)
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    font = pygame.font.Font(None, 30)

    while True:
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        for col in range(4):
            for row in range(4):
                text = font.render(str(game[col][row]), 1, (10, 10, 10))
                background.blit(text, (100+40*row, 20+40*col))

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game = move_up(game)

                if event.key == pygame.K_DOWN:
                    game = move_down(game)

                if event.key == pygame.K_RIGHT:
                    game = move_right(game)

                if event.key == pygame.K_LEFT:
                    game = move_left(game)


def show_game(game):
    for row in game:
        print(row)
    print("\n")

if __name__ == "__main__":
    main()

