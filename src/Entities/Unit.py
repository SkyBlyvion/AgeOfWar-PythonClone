import pygame

class Unit:
    def __init__(self, x, y, width, height, speed, attack_damage, target_building):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.attack_damage = attack_damage
        self.target_building = target_building
        self.alive = True

    def move(self):
        """Move the unit towards the enemy building."""
        self.x += self.speed

        # Check if unit has reached the building
        if self.x + self.width >= self.target_building.x:
            self.target_building.take_damage(self.attack_damage)
            self.alive = False  # Unit disappears after hitting the building

    def draw(self, surface):
        """Draw the unit."""
        pygame.draw.rect(surface, (0, 0, 255), (self.x, self.y, self.width, self.height))
