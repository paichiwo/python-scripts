import pygame

pygame.init()
window = pygame.display.set_mode((320, 180))
clock = pygame.time.Clock()

corner_points = [(-50, 50), (250, 50), (250, 100), (100, 150)]
pos = corner_points[0]
speed = 1


class Paths:
    def __init__(self):
        super().__init__()

        self.patterns = {
            "trapezoid_1": [(-50, 50), (250, 50), (250, 100), (100, 150)]
        }

        self.pattern_index = 0
        self.position = self.patterns["trapezoid_1"][self.pattern_index]
        self.speed = 1

    def movement(self, pattern):
        direction = pygame.math.Vector2(pattern[0]) - pos
        if direction.length() <= self.speed:
            self.position = pattern[0]
            pattern.append(pattern[0])
            pattern.pop(0)
        else:
            direction.scale_to_length(speed)
            new_position = pygame.math.Vector2(pos) + direction
            self.position = (new_position.x, new_position.y)
        return self.position


image = pygame.image.load('assets/img/ship/middle.png').convert_alpha()
path = Paths()

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos = path.movement(path.patterns["trapezoid_1"])
    image_rect = image.get_rect(center=pos)

    window.fill(0)
    pygame.draw.lines(window, "gray", True, corner_points)
    window.blit(image, image_rect)
    pygame.display.update()

pygame.quit()
exit()