import pygame

def draw_health_bar(surface, x, y, current_health, max_health, width=100, height=10):
    """
    Draw a health bar on the given surface.
    
    :param surface: Pygame surface on which to draw
    :param x: The x-coordinate of the health bar
    :param y: The y-coordinate of the health bar
    :param current_health: Current health value
    :param max_health: Maximum health value
    :param width: Width of the health bar
    :param height: Height of the health bar
    """
    # Red background for full health bar
    pygame.draw.rect(surface, (255, 0, 0), (x, y, width, height))
    
    # Green foreground representing current health
    health_percentage = current_health / max_health
    pygame.draw.rect(surface, (0, 255, 0), (x, y, width * health_percentage, height))

def handle_collisions(units):
    """
    Handle unit-to-unit collisions and other interactions.
    
    :param units: A list of all units on the battlefield
    """
    # Collision logic will go here
    pass
