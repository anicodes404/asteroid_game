import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


# Use an infinite while loop for the game loop. At each iteration, it should:
# Call log_state() – no arguments needed.
# Use the screen's .fill method to fill the screen with a solid "black" color (you can literally just pass the string "black" to the method).
# Use pygame's display.flip() method to refresh the screen. Be sure to call this last!





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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )

    player = Player(x_center, y_center, updatable, drawable)
    asteroid_field = AsteroidField()
    
    while True: 
        log_state()
        dt = clock.tick(60) / 1000 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return 
            
        updatable.update(dt)
        
        screen.fill("black")
        # time.tick(60)

        
        # print(len(drawable), len(updatable))
    

        for obj in drawable: 
            obj.draw(screen)

           


        pygame.display.flip()


if __name__ == "__main__":
    main()
