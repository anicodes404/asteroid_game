from circleshape import CircleShape
import pygame
import random
from constants import *
from logger import log_event

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

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first = self.velocity.rotate(angle)
            second = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = first * 1.2
            second_asteroid.velocity = second * 1.2
            
            
        






