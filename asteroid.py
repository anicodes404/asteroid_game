from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        center = self.position
        radius = self.radius
        line_width = LINE_WIDTH
        pygame.draw.circle(screen, color, center, radius, line_width)

    def update(self, dt):
        movement = self.velocity * dt
        self.position += movement
        






