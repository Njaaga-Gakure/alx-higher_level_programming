#!/usr/bin/python3
"""Rectangle class module."""


from .base import Base


class Rectangle(Base):
    """A class that defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Construct a rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set and Get width of a rectangle instance."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set and Get height of a rectangle instance."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set and Get x."""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set and Get y."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of a Rectangle instance."""
        return (self.width * self.height)

    def display(self):
        """Print a Rectangle instance."""
        for a in range(self.y):
            print("")
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Update attributes of a Retcangle instance."""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """Return a string representation of a Rectangle instance."""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y,
                        self.width, self.height))

    def to_dictionary(self):
        """Return a dictionary representation of a Rectangle."""
        return ({
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                })
