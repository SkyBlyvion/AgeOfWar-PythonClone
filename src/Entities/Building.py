import pygame

from Utils import draw_health_bar

class Building:
    def __init__(self, x, y, width, height, max_health=4000, age=0, is_enemy=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health
        self.age = age  # Track the current age for the building
        self.turrets = []
        self.max_turrets = 1
        self.upgrades = 0
        
        # Load the base building sprite based on the age (e.g., 1.png, 2.png)
        self.base_sprite = pygame.image.load(f"./Assets/sprites/bases/{self.age + 1}.png")

        # Flip the building horizontally if it's an enemy building
        if is_enemy:
            self.base_sprite = pygame.transform.flip(self.base_sprite, True, False)  # Flip horizontally

        # Load the turret sprite and floor sprite if applicable
        self.turret_sprite = pygame.image.load(f"./Assets/sprites/turrets/{self.age + 1}.png")
        
    def upgrade_building(self):
        """Upgrade the building to add a floor and allow for more turrets."""
        if self.upgrades < 2:  # Allow up to 2 upgrades
            self.upgrades += 1
            self.max_turrets += 1  # Each upgrade allows for one more turret

    def can_add_turret(self):
        """Check if more turrets can be added to this building."""
        return len(self.turrets) < self.max_turrets

    def take_damage(self, amount):
        """Reduce health by a certain amount."""
        self.current_health = max(0, self.current_health - amount)

    def draw(self, surface):
        """Draw the building, its floor (if any), and its turrets."""
        
        # Draw the base building sprite
        surface.blit(self.base_sprite, (self.x, self.y))

        # Draw the health bar above the building
        draw_health_bar(
            surface, self.x + 100, self.y - 15, self.current_health, self.max_health,
        )

        # Draw the turret(s)
        self.draw_turrets(surface)

    def draw_turrets(self, surface):
        """Draw turrets on the building, up to the allowed number."""
        turret_offset = self.base_sprite.get_width() // (self.max_turrets + 1)  # Dynamically calculate offset
        for i, turret in enumerate(self.turrets):
            surface.blit(turret.sprite, (self.x + (i + 1) * turret_offset - turret.width // 2, self.y - turret.height))
