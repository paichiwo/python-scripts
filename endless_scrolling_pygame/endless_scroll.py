import pygame
import math

pygame.init()

window_height = 600
image_height = 800
scroll = 0


def scrolling():
    """Endless scroll method"""
    panels = math.ceil(window_height / image_height + 2)

    scroll += 4
    for i in range(panels):
        y_pos = int((i * image_height) + scroll - image_height)
        screen.blit(image, (0, y_pos))
        if abs(scroll) >= image_height:
            scroll = 0