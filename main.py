import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # ---- NEW GROUPS ----
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # ---- register containers BEFORE creating player ----
    Player.containers = (updatable, drawable)

    # create player (auto-added to both groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # ---- UPDATE via group ----
        updatable.update(dt)

        # ---- DRAW via group ----
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
