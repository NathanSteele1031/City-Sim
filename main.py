import pygame, colors

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill(colors.GREEN)
        pygame.display.flip()

if __name__ == "__main__":
    main()