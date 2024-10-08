import pygame

class Unit:
    def __init__(self, x, y, width, height, speed, attack_damage, target_building, color, max_health=3, attack_cooldown=60, sprite=None, is_enemy=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.attack_damage = attack_damage
        self.target_building = target_building
        self.alive = True
        self.color = color
        self.max_health = max_health
        self.current_health = max_health
        self.attack_cooldown = attack_cooldown # Attack cooldown in seconds
        self.last_attack_time = 0 # Initialize the last attack time
        self.in_combat = False  # New attribute to track if the unit is in combat
        self.sprite = sprite  # Store the sprite for the unit

        # Flip the sprite horizontally if this is an enemy unit
        if is_enemy:
            self.sprite = pygame.transform.flip(self.sprite, True, False)  # Flip horizontally

    def take_damage(self, damage):
        """Reduce the unit's health by a certain amount."""
        self.current_health -= damage
        if self.current_health <= 0:
            self.alive = False  # The unit dies when health reaches 0
            self.in_combat = False  # No longer in combat if dead

    def move(self):
        """Move the unit towards the enemy building only if not in combat."""
        if not self.in_combat:  # Only move if not in combat
            self.x += self.speed

    def can_attack(self, current_time):
        """Check if the unit can attack based on cooldown."""
        return current_time - self.last_attack_time >= self.attack_cooldown

    def draw_health_bar(self, surface, health_bar_x=None):
        """Draw the health bar above the unit."""
        
        # Use the unit's X position if no custom health bar X position is provided
        if health_bar_x is None:
            health_bar_x = self.x +80
        
        health_percentage = self.current_health / self.max_health
        
        # Draw the red background for full health
        pygame.draw.rect(surface, (255, 0, 0), (health_bar_x, self.y - 10, self.width, 5))
        
        # Draw the green foreground representing current health
        pygame.draw.rect(surface, (0, 255, 0), (health_bar_x, self.y - 10, self.width * health_percentage, 5))

    def draw(self, surface):
        """Draw the unit and its health bar."""
        if self.sprite:
            surface.blit(self.sprite, (self.x, self.y))  # Draw the sprite instead of a rectangle
        else:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height)) # Draw the rectangle
        
        # Draw the health bar
        self.draw_health_bar(surface)
