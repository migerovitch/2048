from moves import *
import pygame


def game_loop(player = "human"):
    grid = [[0, 0, 0, 0] for _ in range(4)]
    grid = add_block(grid)

    score = 0

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 300))
    font_normal = pygame.font.Font(None, 30)
    BLACK = (10, 10, 10)
    font_large = pygame.font.Font(None, 50)

    while not is_game_over(grid):
        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        for col in range(4):
            for row in range(4):
                text = font_normal.render(str(grid[col][row]), 1, BLACK)
                background.blit(text, (100+50*row, 20+50*col))

        rect = pygame.draw.rect(background, (0,0,0), (300, 60, 260, 50), 2)
        background.blit(font_large.render("Score: " + str(score), 1, BLACK), (310, 70))
        pygame.display.update()

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()

        if player == "human":

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        grid, score = move_up(grid, score)

                    if event.key == pygame.K_DOWN:
                        grid, score = move_down(grid, score)

                    if event.key == pygame.K_RIGHT:
                        grid, score = move_right(grid, score)

                    if event.key == pygame.K_LEFT:
                        grid, score = move_left(grid, score)

        else:
            pass
    show_board(grid)
    print(score)
