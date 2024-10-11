import pygame

class Turret:
    def __init__(self, x, y, width, height, attack_damage, attack_cooldown, sprite=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.attack_damage = attack_damage
        self.attack_cooldown = attack_cooldown  # Attack cooldown in milliseconds
        self.last_attack_time = 0
        self.alive = True
        self.sprite = sprite  # Sprite image of the turret

    def can_attack(self, current_time):
        """Check if the turret can attack based on the cooldown."""
        return current_time - self.last_attack_time >= self.attack_cooldown

    def attack(self, target):
        """Attack the target, reducing its health."""
        target.take_damage(self.attack_damage)
        self.last_attack_time = pygame.time.get_ticks()

    def draw(self, surface):
        """Draw the turret on the given surface."""
        if self.sprite:
            surface.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
