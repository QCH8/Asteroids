import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player

def main():
    pygame.init()
    main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #main_screen.fill("black")
        main_screen.fill((0,0,0))
        player.draw(main_screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
