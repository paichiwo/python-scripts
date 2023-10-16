import pygame
import sys
import math

pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sinusoidal Path")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)


def generate_circular_path(radius, center_x, center_y):
    path = []
    for angle in range(360):
        radian_angle = math.radians(angle)
        x = center_x + radius * math.cos(radian_angle)
        y = 1
        path.append((x, y))
    return path


radius = 300
center_x = screen_width // 2
center_y = screen_height // 2
circular_path = generate_circular_path(radius, center_x, center_y)


def generate_sinusoidal_path(screen_width, amplitude, frequency):
    path = []
    for x in range(screen_width):
        y = amplitude * math.sin(2 * math.pi * frequency * x / screen_width) + screen_height / 2
        path.append((x, y))
    print(path)
    return path


amplitude = 100
frequency = 5
sinusoidal_path = generate_sinusoidal_path(screen_width, amplitude, frequency)


class Follower:
    def __init__(self, path):
        self.path = path
        self.index = 0
        self.x, self.y = path[0]

    def follow_path(self):
        if self.index < len(self.path):
            self.x, self.y = self.path[self.index]
            self.index += 1


follower = Follower(circular_path)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    follower.follow_path()

    # Draw an unfilled rectangle at the current position of the follower
    rect_width = 20  # Adjust as needed
    rect_height = 40  # Adjust as needed
    pygame.draw.rect(screen, red, (int(follower.x), int(follower.y), rect_width, rect_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
