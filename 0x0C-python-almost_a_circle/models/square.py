#!/usr/bin/python3
"""Square class module."""


from .rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Construct a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set and get size of a Square instance."""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update a Square instance."""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """Return a string representation of a Square instance."""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        """Return a dictionary representation of a Rectangle."""
        return ({
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                })
