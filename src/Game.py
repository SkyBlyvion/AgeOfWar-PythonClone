import pygame
from Entities.Building import Building
from Entities.Unit import Unit

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.buildings = {
            "player": Building(50, 450, 100, 150),
            "enemy": Building(650, 450, 100, 150)
        }
        self.units = []
        self.spawn_timer = 0

    def spawn_unit(self, side):
        """Spawn a unit for the player or the enemy."""
        if side == "player":
            unit = Unit(150, 500, 40, 40, 2, 10, self.buildings["enemy"])
        else:
            unit = Unit(600, 500, 40, 40, -2, 10, self.buildings["player"])
        self.units.append(unit)

    def update(self):
        """Update the game state."""
        self.spawn_timer += 1
        if self.spawn_timer >= 120:  # Spawn a unit every 2 seconds
            self.spawn_unit("player")
            self.spawn_unit("enemy")
            self.spawn_timer = 0

        # Update all units
        for unit in self.units[:]:
            unit.move()
            if not unit.alive:
                self.units.remove(unit)

    def draw(self):
        """Draw all game elements."""
        self.screen.fill((255, 255, 255))  # Clear the screen

        # Draw buildings
        self.buildings["player"].draw(self.screen)
        self.buildings["enemy"].draw(self.screen)

        # Draw units
        for unit in self.units:
            unit.draw(self.screen)
