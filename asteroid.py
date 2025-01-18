import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="whitesmoke",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        turn_left = self.velocity.rotate(-split_angle)
        turn_right = self.velocity.rotate(split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        left = Asteroid(*self.position, new_radius)
        left.velocity = turn_left * 1.2
        right = Asteroid(*self.position, new_radius)
        right.velocity = turn_right * 1.2
