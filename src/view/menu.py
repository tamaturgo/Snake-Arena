import pygame
from src.view import arena
from src.view import credits
from src.constant import WINDOW_WIDTH, WINDOW_HEIGHT, click_SFX

# Menu Assets
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")


# Menu
def menu():
    cycle = True
    click = False
    while cycle:
        menu_bg = pygame.image.load("assets/images/menu.png")
        if 480 < pygame.mouse.get_pos()[0] < 714:
            if 215 < pygame.mouse.get_pos()[1] < 290:
                menu_bg = pygame.image.load("assets/images/menu_play.png")
                if click:
                    click = False
                    click_SFX.play()
                    arena.reset_game()
                    arena.main()
            if 320 < pygame.mouse.get_pos()[1] < 400:
                menu_bg = pygame.image.load("assets/images/menu_credits.png")
                if click:
                    click = False
                    click_SFX.play()
                    credits.credits_menu()
            if 430 < pygame.mouse.get_pos()[1] < 520:
                menu_bg = pygame.image.load("assets/images/menu_quit.png")
                if click:
                    click_SFX.play()
                    pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cycle = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        window.blit(menu_bg, (0,0))
        pygame.display.flip()


if __name__ == '__main__':
    menu()
