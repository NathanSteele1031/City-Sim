import pygame, colors, roads

class Building:
    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self._rotation = rotation

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation % 360
    
    def draw(self, screen: pygame.Surface): 
        # Need to know the valid place to put buildings on roads
        # Need to know the rotation so the buildings are alined with the roads
        buildingImg = pygame.image.load("Images/BlankBuilding.png")
        buildingImg = pygame.transform.rotate(buildingImg, self._rotation)
        screen.blit(buildingImg, (self.x, self.y))