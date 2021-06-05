import random
import pygame
from src.constant import BALL_SIZE


def init_ball():
    ball_x = random.randint(100, 1100)
    return pygame.Rect(ball_x, 72, BALL_SIZE, BALL_SIZE)
