import pygame
import sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot



def main():
    print("Starting Asteroids with pygame verison VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()

    x_center = int(SCREEN_WIDTH / 2)
    y_center = int(SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)

    player = Player(x_center, y_center, updatable, drawable)
    asteroid_field = AsteroidField()
    
    while True: 
        log_state()
        dt = clock.tick(60) / 1000 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return 
            
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                 if asteroid.collides_with(shot):
                      log_event("asteroid_shot")
                      asteroid.split()
                      shot.kill()
                      

            if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
        
        screen.fill("black")
        # time.tick(60)

        
        # print(len(drawable), len(updatable))
    

        for obj in drawable: 
            obj.draw(screen)

           


        pygame.display.flip()


if __name__ == "__main__":
    main()
