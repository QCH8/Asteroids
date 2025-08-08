import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from constants import PLAYER_RADIUS, PLAYER_ROTATION_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    dt = 0
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #main_screen.fill("black")
        main_screen.fill((0,0,0))
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision_detection(shot):
                    asteroid.split()
                    shot.kill()
                

        for i in drawable:
            i.draw(main_screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
