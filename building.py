import pygame

class Building:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen: pygame.Surface): 
        # Need to know the valid place to put buildings on roads
        # Need to know the rotation so the buildings are alined with the roads
        pass