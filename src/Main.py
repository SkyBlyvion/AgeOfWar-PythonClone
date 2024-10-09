import pygame
import sys
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

# Load the menu sprite (menu that will be displayed on top-right corner)
action_menu_sprite = pygame.image.load('./Assets/sprites/1 1.png')  # This sprite will represent your menu
unit_menu_sprite = pygame.image.load('./Assets/sprites/troop icons/1.png')  # For unit icons if needed
turret_menu_sprite = pygame.image.load('./Assets/sprites/turret icons/1.png')  # For turret icons if needed

# Define clickable areas (rectangles) for the in-game menu buttons
in_game_menu_buttons = [
    pygame.Rect(WIDTH - 300, 50, 32, 32),  # First button (e.g., spawn unit)
    pygame.Rect(WIDTH - 260, 50, 32, 32),  # Second button (e.g., buy turret)
    pygame.Rect(WIDTH - 220, 50, 32, 32),  # Third button (e.g., sell turret)
    pygame.Rect(WIDTH - 180, 50, 32, 32),  # Fourth button (e.g., upgrade building)
    pygame.Rect(WIDTH - 140, 50, 32, 32),  # Fifth button (e.g., upgrade age)
]

# Define clickable areas (rectangles) for the in-game menu buttons
unit_menu_buttons = [
    pygame.Rect(WIDTH - 300, 50, 32, 32),  # First button (e.g., spawn unit)
    pygame.Rect(WIDTH - 260, 50, 32, 32),  # Second button
    pygame.Rect(WIDTH - 220, 50, 32, 32),  # Third button
    pygame.Rect(WIDTH - 130, 50, 32, 32),  # Back arrow to return to the in-game menu
]

# Define clickable areas (rectangles) for the turret_menu buttons
turret_menu_buttons = [
    pygame.Rect(WIDTH - 300, 50, 32, 32),  # First button (e.g., spawn unit)
    pygame.Rect(WIDTH - 260, 50, 32, 32),  # Second button
    pygame.Rect(WIDTH - 220, 50, 32, 32),  # Third button
    pygame.Rect(WIDTH - 130, 50, 32, 32),  # Back arrow to return to the in-game menu
]

# Game states
GAME_PLAY = 'game_play' # Base Menu
UNIT_MENU = 'unit_menu' # Unit Menu
TURRET_MENU = 'turret_menu' # Turret Menu
current_menu = GAME_PLAY  # Start the game directly

# Initialize the game (normal gameplay)
game = Game(screen, font)

# Function to handle user clicks in the in-game action menu
def handle_in_game_action_menu_click(mouse_pos):
    """Handle clicks in the in-game action menu."""
    global current_menu
    for i, rect in enumerate(in_game_menu_buttons):
        if rect.collidepoint(mouse_pos):
            if i == 0:
                print("First button (unit menu) clicked!")
                # Switch to the unit selection menu
                current_menu = UNIT_MENU
            elif i == 1:
                print("Buy turret clicked!")
                # Code to buy turret goes here
                current_menu = TURRET_MENU
            elif i == 2:
                print("Sell turret clicked!")
                # Code to sell turret goes here
            elif i == 3:
                print("Upgrade building clicked!")
                # Code to upgrade building goes here
            elif i == 4:
                print("Upgrade age clicked!")
                # Code to upgrade the age goes here

# Function to handle user clicks in the unit menu
def handle_unit_menu_click(mouse_pos):
    """Handle clicks in the unit selection menu."""
    global current_menu
    for i, rect in enumerate(unit_menu_buttons):
        if rect.collidepoint(mouse_pos):
            if i == 0:
                print("First unit selected!")
                # Code to spawn the first unit
                game.spawn_unit("player", 0)
            elif i == 1:
                print("Second unit selected!")
                # Code to spawn the second unit
                game.spawn_unit("player", 1)
            elif i == 2:
                print("Third unit selected!")
                # Code to spawn the third unit
                game.spawn_unit("player", 2)
            elif i == 3:
                print("Back arrow clicked! Returning to the in-game action menu.")
                # Return to the in-game action menu
                current_menu = GAME_PLAY

# Function to handle user clicks in the turret menu
def handle_turret_menu_click (mouse_pos):
    """Handle clicks in the turret selection menu."""
    global current_menu
    for i, rect in enumerate(turret_menu_buttons):
        if rect.collidepoint(mouse_pos):
            if i == 0:
                print("First turret selected!")
                # Code to spawn the first turret
                game.spawn_turret("player", 0)
            elif i == 1:
                print("Second turret selected!")
                # Code to spawn the second turret
                game.spawn_turret("player", 1)
            elif i == 2:
                print("Third turret selected!")
                # Code to spawn the third turret
                game.spawn_turret("player", 2)
            elif i == 3:
                print("Back arrow clicked! Returning to the in-game action menu.")
                # Return to the in-game action menu
                current_menu = GAME_PLAY

# Function to draw the in-game action menu
def draw_in_game_action_menu(screen):
    """Draw the in-game action menu on the top-right corner."""
    # Draw the menu sprite on the top-right corner
    screen.blit(action_menu_sprite, (WIDTH - 300, 50))
    
    # Draw clickable buttons for the menu
    for rect in in_game_menu_buttons:
        pygame.draw.rect(screen, (255, 0, 0), rect, 2)  # Red borders for buttons (for debugging)

# Function to draw the unit selection menu
def draw_unit_menu(screen):
    """Draw the unit selection menu."""
    # Draw the unit menu sprite
    screen.blit(unit_menu_sprite, (WIDTH - 300, 50))
    
    # Draw clickable buttons for units
    for rect in unit_menu_buttons:
        pygame.draw.rect(screen, (0, 255, 0), rect, 2)  # Green borders for buttons (for debugging)

# Function to draw the turret selection menu
def draw_turret_menu(screen):
    """Draw the turret selection menu."""
    # Draw the unit menu sprite
    screen.blit(turret_menu_sprite, (WIDTH - 300, 50))
    
    # Draw clickable buttons for units
    for rect in turret_menu_buttons:
        pygame.draw.rect(screen, (0, 255, 0), rect, 2)  # Green borders for buttons (for debugging)

# Main game loop
def main():
    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear the screen with white background

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_menu == GAME_PLAY: 
                    handle_in_game_action_menu_click(event.pos)  # Handle clicks in the in-game menu
                elif current_menu == UNIT_MENU:
                    handle_unit_menu_click(event.pos)  # Handle clicks in the unit selection menu
                elif current_menu == TURRET_MENU:
                    handle_turret_menu_click(event.pos) # Code to handle clicks in the turret selection menu 

        # Update and draw the game elements
        game.update()  # Update game logic (units, buildings, etc.)
        game.draw()    # Draw the game elements (units, buildings, etc.)

        # Draw the appropriate menu based on the current menu state
        if current_menu == GAME_PLAY:
            draw_in_game_action_menu(screen)  # Draw in-game action menu
        elif current_menu == UNIT_MENU:
            draw_unit_menu(screen)  # Draw unit selection menu
        elif current_menu == TURRET_MENU:
            draw_turret_menu(screen)  # Draw turret selection menu

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()