import random

apple_pos_xy = []


def create_apple():
    pos_x = 40 + random.randint(0, 34) * 32
    pos_y = 72 + random.randint(0, 17) * 32
    pos_xy = (pos_x, pos_y)
    return pos_xy
