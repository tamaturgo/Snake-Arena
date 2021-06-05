import pygame
from src.constant import WINDOW_WIDTH, WINDOW_HEIGHT, click_SFX, font_20, font_30
import menu

# Menu Assets
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")


# Menu
def credits_menu():
    cycle = True
    click = False
    while cycle:
        menu_bg = pygame.image.load("assets/images/credits.png")
        if 480 < pygame.mouse.get_pos()[0] < 714:
            if 515 < pygame.mouse.get_pos()[1] < 590:
                menu_bg = pygame.image.load("assets/images/credits_pressed.png")
                if click:
                    click = False
                    menu.menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                click_SFX.play()

        window.blit(menu_bg, (0, 0))

        initial_text = font_30.render('Developer',
                                      True, (50, 50, 50))
        initial_text_rect = initial_text.get_rect()
        initial_text_rect.center = (600, 180)
        window.blit(initial_text, initial_text_rect)
        initial_text = font_20.render('Diogeles Tamaturgo',
                                      True, (50, 50, 50))
        initial_text_rect = initial_text.get_rect()
        initial_text_rect.center = (600, 220)
        window.blit(initial_text, initial_text_rect)

        initial_text = font_30.render('Sounds',
                                      True, (50, 50, 50))
        initial_text_rect = initial_text.get_rect()
        initial_text_rect.center = (600, 300)
        window.blit(initial_text, initial_text_rect)

        initial_text = font_20.render('Music By BloodPixel',
                                      True, (50, 50, 50))
        initial_text_rect = initial_text.get_rect()
        initial_text_rect.center = (600, 340)
        window.blit(initial_text, initial_text_rect)

        initial_text = font_20.render('SFX By Jofae; InspectorJ; jhyland.',
                                      True, (50, 50, 50))
        initial_text_rect = initial_text.get_rect()
        initial_text_rect.center = (600, 370)
        window.blit(initial_text, initial_text_rect)

        pygame.display.flip()


if __name__ == '__main__':
    credits_menu()
