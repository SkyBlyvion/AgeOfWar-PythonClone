import pygame

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
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))

        # Health bar
        health_bar_width = 100
        health_bar_height = 10
        health_percentage = self.current_health / self.max_health
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y - 15, health_bar_width, health_bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y - 15, health_bar_width * health_percentage, health_bar_height))
