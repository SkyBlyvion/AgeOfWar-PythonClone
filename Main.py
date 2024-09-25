import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Age of War Clone")

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game clock
clock = pygame.time.Clock()
FPS = 60

class Building:
    def __init__(self, x, y, width, height, max_health=4000):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, amount):
        """Reduce health by a certain amount."""
        self.current_health = max(0, self.current_health - amount)

    def draw(self, surface):
        """Draw the building and its health bar."""
        # Draw the building as a rectangle
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height))

        # Draw the health bar
        health_bar_width = 100
        health_bar_height = 10
        health_percentage = self.current_health / self.max_health
        pygame.draw.rect(surface, RED, (self.x, self.y - 15, health_bar_width, health_bar_height))  # Red background (full health bar)
        pygame.draw.rect(surface, GREEN, (self.x, self.y - 15, health_bar_width * health_percentage, health_bar_height))  # Green foreground (current health)

# Create two buildings, one on each side
player_building = Building(50, HEIGHT - 150, 100, 150)
enemy_building = Building(WIDTH - 150, HEIGHT - 150, 100, 150)

# Main game loop
def main():
    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Simulate damage to the enemy building for testing
        enemy_building.take_damage(1)  # Take 1 damage per frame

        # Clear screen
        screen.fill(WHITE)

        # Draw the buildings and health bars
        player_building.draw(screen)
        enemy_building.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
