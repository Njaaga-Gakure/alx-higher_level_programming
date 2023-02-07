#!/usr/bin/python3
"""class Square module."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square."""

    def __init__(self, size):
        """Create a class Square instance."""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Return area of class Square instance."""
        return (self.__size ** 2)
