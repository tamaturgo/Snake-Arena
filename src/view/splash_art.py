import time
import pygame
from src.view import menu
from src.constant import WINDOW_WIDTH, WINDOW_HEIGHT
# Start Screen Assets
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")


# Start Screen Function
def main():
    window.blit(pygame.image.load("assets/images/splash_art.png"), (0, 0))
    pygame.display.update()
    time.sleep(10)
    menu.menu()


if __name__ == '__main__':
    main()
