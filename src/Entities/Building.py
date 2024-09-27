import pygame

from Utils import draw_health_bar

class Building:
    def __init__(self, x, y, width, height, max_health=4000, age=0, has_floor=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health
        self.age = age  # Track the current age for the building
        self.has_floor = has_floor  # If the building has a +1 floor
        
        # Load the base building sprite based on the age (e.g., 1.png, 2.png)
        self.base_sprite = pygame.image.load(f"./Assets/sprites/bases/{self.age + 1}.png")

        # Load the turret sprite and floor sprite if applicable
        self.turret_sprite = pygame.image.load(f"./Assets/sprites/turrets/{self.age + 1}.png")
        if self.has_floor:
            self.floor_sprite = pygame.image.load(f"./Assets/sprites/bases/{self.age + 1}.png")

    def take_damage(self, amount):
        """Reduce health by a certain amount."""
        self.current_health = max(0, self.current_health - amount)

    def draw(self, surface):
        """Draw the building, its floor (if any), and its turrets."""
        
        # Draw the base building sprite
        surface.blit(self.base_sprite, (self.x, self.y))

        # Draw the health bar above the building
        draw_health_bar(
            surface,
            self.x + 100,
            self.y - 15,
            self.current_health,
            self.max_health,
        )

        # Draw the floor if the building has a +1 floor
        if self.has_floor:
            surface.blit(self.floor_sprite, (self.x, self.y - self.base_sprite.get_height()))  # Draw floor above the building

        # Draw the turret(s)
        self.draw_turrets(surface)

    def draw_turrets(self, surface):
        """Draw one or two turrets on the building."""
        
        # If the building has a +1 floor, draw two turrets
        if self.has_floor:
            turret_offset = self.base_sprite.get_width() // 4  # Calculate spacing for turrets
            surface.blit(self.turret_sprite, (self.x + turret_offset, self.y - self.turret_sprite.get_height()))
            surface.blit(self.turret_sprite, (self.x + 3 * turret_offset, self.y - self.turret_sprite.get_height()))
        else:
            # Draw one turret centered on the building
            turret_offset = self.base_sprite.get_width() // 2 - self.turret_sprite.get_width() // 2
            surface.blit(self.turret_sprite, (self.x + turret_offset, self.y - self.turret_sprite.get_height()))
