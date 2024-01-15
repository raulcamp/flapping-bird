"""Game of Life"""
import sys
import pygame
from constants import (
    WIDTH,
    HEIGHT,
    WHITE,
)


class Game:
    """Represents a game"""
    def __init__(self):
        pass

    def update(self):
        """Update game state"""
        pass

    def draw(self, screen):
        """Draw the current game objects"""
        pass


def draw_rect(screen, obj):
    """Draws a Pygame rectangle"""
    x, y, size = (obj.x * obj.size) + 1, (obj.y * obj.size) + 1, obj.size - 1
    pygame.draw.rect(screen, obj.color, (x, y, size, size))


def draw_grid(screen):
    """Draws a grid"""
    pass


def main():
    """Initializes and runs the game"""
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game()

    # Fill the background
    screen.fill(WHITE)
    draw_grid(screen)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_1:
                    pass
                if event.key == pygame.K_2:
                    pass
            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pass
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pass
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass

        # Draw the grid and current state
        game.draw(screen)
        # Update the game state
        game.update()
        # Update the display
        pygame.display.update()
        # Set the framerate
        clock.tick(60)


if __name__ == "__main__":
    main()
