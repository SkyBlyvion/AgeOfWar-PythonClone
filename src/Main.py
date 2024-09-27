import pygame
from Game import Game

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 1280, 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Age of War Clone")

# Initialize font for displaying health numbers
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)  # You can change 'Arial' and size as needed

# Set up the game clock
clock = pygame.time.Clock()
FPS = 60

# Initialize the game
game = Game(screen, font)

# Main game loop
def main():
    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update game logic
        game.update()

        # Draw everything
        game.draw()

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
