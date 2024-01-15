"""Flapping Bird entities, objects, and classes"""
from dataclasses import dataclass


@dataclass
class Point:
    """Represents a point in 2D space"""
    x: int
    y: int

    def get(self):
        """Returns the coordinates of the point"""
        return self.x, self.y


@dataclass
class Object:
    """Represents an object"""
    coordinates: Point
    width: int
    height: int
    color: tuple


@dataclass
class Bird(Object):
    """Represents a Bird"""

    def get_pos(self):
        """Returns the position of the bird"""
        return self.coordinates.get()

    def set_pos(self, coordinates):
        """Sets the position of the bird"""
        x, y = coordinates
        self.coordinates = Point(x, y)

    def move(self, dx, dy):
        """Moves the bird"""
        x, y = self.coordinates.get()
        self.set_pos((x + dx, y + dy))

    def get_width(self):
        """Returns the width of the bird"""
        return self.width

    def get_height(self):
        """Returns the height of the bird"""
        return self.height

    def get_color(self):
        """Returns the color of the bird"""
        return self.color


@dataclass
class Pipe(Object):
    """Represents a Pipe"""

    def get_pos(self):
        """Returns the position of the pipe"""
        return self.coordinates.get()

    def set_pos(self, coordinates):
        """Sets the position of the pipe"""
        x, y = coordinates
        self.coordinates = Point(x, y)

    def move(self, dx, dy):
        """Moves the pipe"""
        x, y = self.coordinates.get()
        self.set_pos((x + dx, y + dy))

    def get_width(self):
        """Returns the width of the pipe"""
        return self.width

    def get_height(self):
        """Returns the height of the pipe"""
        return self.height

    def get_color(self):
        """Returns the color of the pipe"""
        return self.color


if __name__ == "__main__":
    pass
