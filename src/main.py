"""Flapping Bird"""
import sys
import pygame
from entities import Point, Object, Bird
from constants import (
    WIDTH,
    HEIGHT,
    GROUND_HEIGHT,
    BIRD_SIZE,
    WHITE,
    BLACK,
    SKY_BLUE,
    GRASS_GREEN,
    BIRD_YELLOW,
    Y_GRAVITY,
    JUMP_HEIGHT,
)


class Game:
    """Represents a game"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        position = Point(self.width // 3 - BIRD_SIZE // 2,
                         self.height // 2 - BIRD_SIZE // 2)
        self.bird = Bird(position, BIRD_SIZE, BIRD_SIZE, BIRD_YELLOW)

    def update(self):
        """Update game state"""
        pass

    def draw(self, screen):
        """Draw the current game objects"""
        x, y = self.bird.get_pos()
        width, height = self.bird.get_width(), self.bird.get_height()
        color = self.bird.get_color()
        draw_rect(screen, BLACK, x, y, width, height)
        draw_rect(screen, color, x+3, y+3, width-6, height-6)


def draw_rect(screen, color, x, y, width, height):
    """Draws a Pygame rectangle"""
    pygame.draw.rect(screen, color, (x, y, width, height))


def draw_background(screen):
    """Draws a background"""
    pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, GROUND_HEIGHT))
    pygame.draw.rect(screen, GRASS_GREEN,
                     (0, GROUND_HEIGHT, WIDTH, HEIGHT // 5))


def main():
    """Initializes and runs the game"""
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game(WIDTH, HEIGHT)

    jumping_start = False
    y_velocity = JUMP_HEIGHT

    while True:
        # Fill the background
        draw_background(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_SPACE:
                    jumping_start = True
                    y_velocity = JUMP_HEIGHT
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

        if jumping_start:
            game.bird.move(0, -y_velocity)
            y_velocity -= Y_GRAVITY

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
