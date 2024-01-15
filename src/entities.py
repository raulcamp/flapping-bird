"""Flapping Bird entities, objects, and classes"""
from dataclasses import dataclass


@dataclass
class Object:
    """Represents an object"""
    x: int
    y: int
    width: int
    height: int
    color: tuple


if __name__ == "__main__":
    pass
