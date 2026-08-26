import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> list["Asteroid"]:
        # This method should return a list of smaller asteroids after splitting
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            # create smaller asteroids
            log_event("asteroid_split")
            angle = uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2

            return [asteroid1, asteroid2] 