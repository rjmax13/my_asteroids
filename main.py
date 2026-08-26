import pygame
from player import Player
from  constants import  SCREEN_WIDTH, SCREEN_HEIGHT
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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        # print(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
