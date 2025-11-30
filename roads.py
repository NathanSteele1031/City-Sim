import pygame

class Road():
    """
    If there is no vlaues when this is created put none in all parameters
    """
    def __init__(self, starting_x, starting_y, ending_x, ending_y):
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.ending_x = ending_x
        self.ending_y = ending_y
    
    def set_starting_point(self, x, y):
        self.starting_x = x
        self.starting_y = y

    def set_ending_point(self, x, y):
        self.ending_x = x
        self.ending_y = y
    
    def get_end_point(self):
        return (self.ending_x, self.ending_y)
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, (0, 0, 0), (self.starting_x, self.starting_y), (self.ending_x, self.ending_y), 5)

class Road_System():
    def __init__(self):
        self.roads = []

    def does_snap(self, x, y):
        for road in self.roads:
            if (road.starting_x + 10 > x > road.starting_x - 10) and (road.starting_y + 10 > y > road.starting_y - 10):
                return True
            if (road.ending_x + 10 > x > road.ending_x - 10) and (road.ending_y + 10 > y > road.ending_y - 10):
                return True
        return False

    def get_snap_position(self, x, y):
        for road in self.roads:
            if (road.starting_x + 10 > x > road.starting_x - 10) and (road.starting_y + 10 > y > road.starting_y - 10):
                return (road.starting_x, road.starting_y)
            if (road.ending_x + 10 > x > road.ending_x - 10) and (road.ending_y + 10 > y > road.ending_y - 10):
                return (road.ending_x, road.ending_y)
        return None
    
    def add_road(self, road: Road):
        self.roads.append(road)
    
    def draw(self, screen: pygame.Surface):
        for road in self.roads:
            road.draw(screen)