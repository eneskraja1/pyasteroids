import pygame
from shot import Shot
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  # NEW
    shots = pygame.sprite.Group()
    # containers (must be set BEFORE instances are created)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)  # NEW
    AsteroidField.containers = (updatable,)  # NEW (not drawable)
    Shot.containers = (shots, updatable, drawable)

    # instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  # NEW

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # update all
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        # draw all
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
