import pygame
from player import Player
from  constants import  SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED
from  logger import log_state



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
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


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
        pygame.display.flip()

if __name__ == "__main__":
    main()
