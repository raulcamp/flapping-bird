"""Flapping Bird"""
import sys
import pygame
import random
from entities import Point, Bird, Pipe
from constants import (
    WIDTH,
    HEIGHT,
    GROUND_HEIGHT,
    BIRD_SIZE,
    BLACK,
    SKY_BLUE,
    GREEN,
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
        self.pipes = []

    def update(self):
        """Update game state"""
        pass

    def add_pipe_barrier(self):
        """Adds two pipes forming a barrier"""
        space_height = random.randint(200, 500)
        top_pipe = Pipe(Point(WIDTH, 0), 100, space_height, GREEN)
        bot_pipe = Pipe(Point(WIDTH, space_height + 200),
                        100, 800 - space_height + 200, GREEN)
        self.pipes.append((top_pipe, bot_pipe))

    def update_pipes(self):
        """Updates the pipes positions"""
        for top, bot in self.pipes:
            x, _ = top.get_pos()
            if x < -top.get_width():
                self.pipes.remove((top, bot))
            else:
                top.move(-5, 0)
                bot.move(-5, 0)

    def pipe_collision(self):
        for top, bot in self.pipes:
            if collision(self.bird, top) or collision(self.bird, bot):
                return True
        return False

    def draw(self, screen):
        """Draw the current game objects"""
        x, y = self.bird.get_pos()
        width, height = self.bird.get_width(), self.bird.get_height()
        color = self.bird.get_color()
        draw_rect(screen, BLACK, x, y, width, height)
        draw_rect(screen, color, x+3, y+3, width-6, height-6)

        for top, bot in self.pipes:
            x, y = top.get_pos()
            width, height = top.get_width(), top.get_height()
            color = top.get_color()
            draw_rect(screen, color, x, y, width, height)
            x, y = bot.get_pos()
            width, height = bot.get_width(), bot.get_height()
            color = bot.get_color()
            draw_rect(screen, color, x, y, width, height)


def collision(obj1, obj2):
    """Checks if two objects collide"""
    obj1x, obj1y = obj1.get_pos()
    obj2x, obj2y = obj2.get_pos()
    if obj1x < obj2x + obj2.width \
            and obj1x + obj1.width > obj2x:
        if obj1y < obj2y + obj2.height \
                and obj1y + obj1.height > obj2y:
            return True
    return False


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
    distance = 100

    while True:
        print()
        for p in game.pipes:
            print(p)
        print()
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

            if distance == 100:
                game.add_pipe_barrier()
            distance -= 1
            if distance <= 0:
                distance = 100
            game.update_pipes()

        if game.pipe_collision():
            return

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
