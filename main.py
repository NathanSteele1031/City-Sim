import pygame, colors, roads

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    running = True

    road_mode = False
    sample_road = None
    road_system = roads.Road_System()

    buildings = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Activate placing roads
                    road_mode = not road_mode

            if event.type == pygame.MOUSEBUTTONDOWN and road_mode: # Place road
                if not sample_road:
                    sample_road = roads.Road(*pygame.mouse.get_pos(), 0, 0)
                else:
                    sample_road.set_ending_point(*pygame.mouse.get_pos())
                    road_system.add_road(sample_road)
                    sample_road = None

        display.fill(colors.GREEN)

        if sample_road:
            sample_road.set_ending_point(*pygame.mouse.get_pos())
            sample_road.draw(display)

        for road in road_system.roads:
            road.draw(display)

        for building in buildings:
            building.draw(display)

        pygame.display.flip()

if __name__ == "__main__":
    main()