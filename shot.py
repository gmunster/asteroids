import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    containers = ()  # Will be set in main.py

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt        