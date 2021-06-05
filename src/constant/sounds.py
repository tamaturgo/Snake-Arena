import pygame

pygame.init()
pygame.mixer.init()
# Sounds
die_SFX = pygame.mixer.Sound("assets/sounds/die.mp3")
die_SFX.set_volume(0.3)
click_SFX = pygame.mixer.Sound("assets/sounds/click.wav")
click_SFX.set_volume(0.7)
apple_SFX = pygame.mixer.Sound("assets/sounds/apple_catcher.wav")
apple_SFX.set_volume(0.5)
pygame.mixer.music.load("assets/sounds/music.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
