import pygame
import os
from Entities.Building import Building
from Entities.Unit import Unit
from Entities.Turret import Turret

class Game:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        # Load the background image
        self.background = pygame.image.load(f"./Assets/sprites/background.png")

        # Optionally scale the background to fit the window size
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

        self.buildings = {
            "player": Building(0, 450, 100, 150, is_enemy=False),
            "enemy": Building(1000, 450, 100, 150, is_enemy=True)
        } # WIDTH, HEIGHT Screen = 1280, 620
        self.units = []
        self.turrets = {
            "player": [],
            "enemy": []
        }
        self.spawn_timer = 0

        # Gold system for both player and enemy
        self.gold = {"player": 1000, "enemy": 1000}

        # Age system
        self.ages = ["Stone Age", "Medieval Age", "Renaissance Age", "Modern Age", "Future Age"]
        self.current_age = 0  # Start with Stone Age
        self.unit_sprites = {
            "player": {
                0: ["1 1.png", "1 2.png", "1 3.png"],
                1: ["2 1.png", "2 2.png", "2 3.png"],
                2: ["3 1.png", "3 2.png", "3 3.png"],
                3: ["4 1.png", "4 2.png", "4 3.png"],
                4: ["5 1.png", "5 2.png", "5 3.png"]
            },
            "enemy": {
                0: ["1 1.png", "1 2.png", "1 3.png"],
                1: ["2 1.png", "2 2.png", "2 3.png"],
                2: ["3 1.png", "3 2.png", "3 3.png"],
                3: ["4 1.png", "4 2.png", "4 3.png"],
                4: ["5 1.png", "5 2.png", "5 3.png"]
            }
        }
        self.turret_sprites = {
            "player": {
                0: ["1.png", "2.png", "3.png"],
                1: ["4.png", "5.png", "6.png"],
                2: ["7.png", "8.png", "9.png"],
                3: ["10.png", "11.png", "12.png"],
                4: ["13.png", "14.png", "15.png"]
            },
            "enemy": {
                0: ["1.png", "2.png", "3.png"],
                1: ["4.png", "5.png", "6.png"],
                2: ["7.png", "8.png", "9.png"],
                3: ["10.png", "11.png", "12.png"],
                4: ["13.png", "14.png", "15.png"]
            }
        }

    def upgrade_building(self, side):
        """Allow the player to upgrade their building."""
        upgrade_cost = 200
        if self.gold[side] >= upgrade_cost:
            building = self.buildings[side]
            if building.upgrades < 2:  # Allow a max of 2 upgrades
                building.upgrade_building()
                self.gold[side] -= upgrade_cost

    def draw_health_text(self, building, x, y):
        """Draw the health of a building as text at the specified coordinates."""
        health_text = self.font.render(f"{building.current_health}/{building.max_health}", True, (0, 0, 0))
        self.screen.blit(health_text, (x, y))  # Use exact X and Y coordinates

    def draw_gold_text(self):
        """Display the gold amount for both the player and enemy."""
        player_gold_text = self.font.render(f"Player Gold: {self.gold['player']}", True, (0, 0, 0))
        #enemy_gold_text = self.font.render(f"Enemy Gold: {self.gold['enemy']}", True, (0, 0, 0))
        self.screen.blit(player_gold_text, (50, 50))
        #self.screen.blit(enemy_gold_text, (1050, 50))

    def spawn_unit(self, side, unit_type):
        """Spawn a unit based on the age and type (1, 2, or 3)."""
        unit_cost = 50
        if self.gold[side] >= unit_cost:
            age = self.current_age
            sprite = pygame.image.load(f"./Assets/sprites/troops/{self.unit_sprites[side][age][unit_type]}")
            if side == "player":
                unit = Unit(100, 500, 40, 40, 2, 10, self.buildings["enemy"], (0, 0, 255), attack_cooldown=900, sprite=sprite)
            else:
                unit = Unit(900, 500, 40, 40, -2, 10, self.buildings["player"], (255, 0, 0), attack_cooldown=900, sprite=sprite, is_enemy=True)

            self.units.append(unit)
            self.gold[side] -= unit_cost  # Deduct gold after spawning
    

    # # def to spawn turrets
    # def spawn_turret(self, side, turret_type):
    #     """Spawn a turret on the building."""
    #     turret_cost = 100
    #     if self.gold[side] >= turret_cost:
    #         age = self.current_age
    #         sprite = pygame.image.load(f"./Assets/sprites/turrets/{self.turret_sprites[side][age][turret_type]}")
    #         building = self.buildings[side]  # Get the building for the side
            
    #         # Calculate the turret position based on the building's position
    #         turret_x = building.x + building.width // 2 - 20  # Center the turret on the building
    #         turret_y = building.y - 40  # Place the turret above the building
            
    #         # Create a new turret instance
    #         turret = Turret(turret_x, turret_y, 40, 40, attack_damage=5, attack_cooldown=1000, sprite=sprite)
            
    #         # Add the turret to the list of turrets for that side
    #         self.turrets[side].append(turret)
    #         self.gold[side] -= turret_cost

    def spawn_turret(self, side, turret_type):
        """Spawn a turret on the building, if the building has available slots."""
        turret_cost = 100
        building = self.buildings[side]
        if self.gold[side] >= turret_cost and building.can_add_turret():
            age = self.current_age
            sprite = pygame.image.load(f"./Assets/sprites/turrets/{self.turret_sprites[side][age][turret_type]}")
            turret_x = building.x + building.width // 2 - 20
            turret_y = building.y - 40
            turret = Turret(turret_x, turret_y, 40, 40, attack_damage=5, attack_cooldown=1000, sprite=sprite)
            building.turrets.append(turret)
            self.gold[side] -= turret_cost

            

    def update(self):
        """Update the game state."""
        current_time = pygame.time.get_ticks()
        self.spawn_timer += 1
        if self.spawn_timer >= 120:  # Spawn a unit every 2 seconds
            self.spawn_unit("player", 0) # Pass unit_type (e.g., 0 for the first unit type in the current age)
            self.spawn_unit("enemy", 0)
            self.spawn_timer = 0

        # Update all units
        for unit in self.units[:]:  # Iterate over a copy of the list to avoid modification issues
            unit.move()

            if not unit.alive:
                # Award gold to the opponent for the kill before removing the unit
                if unit.color == (0, 0, 255):  # If the unit is a player unit
                    self.gold['enemy'] += 70
                else:  # If the unit is an enemy unit
                    self.gold['player'] += 70

                # Remove the unit after awarding gold
                self.units.remove(unit)
        
        # Handle turret attacks
        for turret in self.turrets["player"]:
            for enemy_unit in [unit for unit in self.units if unit.color == (255, 0, 0)]:
                if turret.can_attack(current_time):
                    turret.attack(enemy_unit)

        for turret in self.turrets["enemy"]:
            for player_unit in [unit for unit in self.units if unit.color == (0, 0, 255)]:
                if turret.can_attack(current_time):
                    turret.attack(player_unit)

        # Handle Combats
        self.handle_combat()

    def draw(self):
        """Draw all game elements."""
        self.screen.fill((255, 255, 255))  # Clear the screen

        # Draw the background
        self.screen.blit(self.background, (0, 0))  # Fill the entire screen with the background image

        # Draw buildings
        self.buildings["player"].draw(self.screen)
        self.buildings["enemy"].draw(self.screen)

        # Draw health numbers for each building
        self.draw_health_text(self.buildings["player"], 100, 400)  # Position near the player building
        self.draw_health_text(self.buildings["enemy"], 1100, 400)  # Position near the enemy building

        # Draw gold text
        self.draw_gold_text()

        # Draw units
        for unit in self.units:
            unit.draw(self.screen)

        # Draw turrets
        for turret in self.turrets["player"]:
            turret.draw(self.screen)

        for turret in self.turrets["enemy"]:
            turret.draw(self.screen)

    def handle_combat(self):
        """Handle combat between friendly and enemy units."""
        current_time = pygame.time.get_ticks()  # Get the current time in milliseconds

        for i in range(len(self.units)):
            for j in range(i + 1, len(self.units)):
                unit_a = self.units[i]
                unit_b = self.units[j]

                # Check if both units are alive and on opposite sides
                if unit_a.alive and unit_b.alive and unit_a.speed > 0 and unit_b.speed < 0:
                    # Check for collision (units overlapping)
                    if unit_a.x + unit_a.width >= unit_b.x and unit_b.x + unit_b.width >= unit_a.x:

                        # Stop both units from moving if they are in combat
                        unit_a.in_combat = True
                        unit_b.in_combat = True

                        # Check if unit A can attack
                        if unit_a.can_attack(current_time):
                            unit_b.take_damage(1)
                            unit_a.last_attack_time = current_time  # Reset attack cooldown for unit A

                        # Check if unit B can attack
                        if unit_b.can_attack(current_time):
                            unit_a.take_damage(1)
                            unit_b.last_attack_time = current_time  # Reset attack cooldown for unit B

                        # If unit A dies, unit B can resume movement
                        if not unit_a.alive:
                            unit_b.in_combat = False  # Unit B can resume moving
                            print(f"Unit A died, Unit B resumes moving. Health: {unit_b.current_health}")

                        # If unit B dies, unit A can resume movement
                        if not unit_b.alive:
                            unit_a.in_combat = False  # Unit A can resume moving
                            print(f"Unit B died, Unit A resumes moving. Health: {unit_a.current_health}")



