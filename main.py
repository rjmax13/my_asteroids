import pygame
import sys
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from  constants import  SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED
from  logger import log_state, log_event



def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    """
    print(f"Starting Asteroids with pygame version: {pygame.ver}")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")
    """

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable, asteroid_field)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        # print(dt)
        screen.fill("black")
        
        for drawable_object in drawable:
            drawable_object.draw(screen)

        updatable.update(dt)

        # iterate over all asteroids
        for all_asteroids in asteroids:
            # check for collisions between the player and each asteroid
            if player.collides_with(all_asteroids):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        # check for collisions between shots and asteroids
        for shot in shots:
            for all_asteroids in asteroids:
                if shot.collides_with(all_asteroids):
                    log_event("asteroid_shot")
                    shot.kill()
                    all_asteroids.split()

        pygame.display.flip()

if __name__ == "__main__":
    main()
