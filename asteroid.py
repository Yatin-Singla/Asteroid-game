from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        # Asteroid-specific update logic goes here
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        split_1_vector = self.velocity.rotate(random_angle)
        split_2_vector = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_1.velocity = split_1_vector * 1.2
        split_asteroid_2.velocity = split_2_vector * 1.2
        
