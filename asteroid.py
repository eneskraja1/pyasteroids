import random
import pygame
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape  # adjust import if your file name differs


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        # this asteroid is always destroyed
        self.kill()

        # small asteroid: no split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # split into 2 smaller asteroids
        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = v1
        a2.velocity = v2

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt
