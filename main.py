import random
from moves import *
import pygame


def main():
    game = [[0, 0, 0, 0] for _ in range(4)]
    game = add_block(game)
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    while 1:
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        for row in range(4):


        # Display some text
        font = pygame.font.Font(None, 30)
        text = font.render(str(game[0]), 1, (10, 10, 10))
        text2 = font.render(str(game[1]), 1, (10, 10, 10))
        text3 = font.render(str(game[2]), 1, (10, 10, 10))
        text4 = font.render(str(game[3]), 1, (10, 10, 10))

        textpos = text.get_rect()
        background.blit(text, (100,10))

        textpos2 = text2.get_rect()
        background.blit(text2, (100,40))

        textpos3 = text3.get_rect()
        background.blit(text3, (100, 70))

        textpos4 = text4.get_rect()
        background.blit(text4, (100, 100))

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Event loop
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

