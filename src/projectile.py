import pygame

class Projectile():
    def __init__(self,start_location, target_location):
        self.location = start_location
        self.target_location = target_location
        self.radius = 1
        self.velocity = 1
        self.color = "yellow"
    
    def draw(self, display):
        pygame.draw.circle(display, self.color, self.location, self.radius)