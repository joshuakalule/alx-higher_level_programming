#!/usr/bin/python3
"""2. First Rectangle."""
from .base import Base


class Rectangle(Base):
    """Rectangle shape class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Set the dimensions for the rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Return the dictionary representation."""
        d = {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y}
        return d

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle instance."""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args is not None:
            for n, attr in enumerate(attrs):
                if n >= len(args):
                    break
                exec(f"self.{attr} = {args[n]}")
        if args and len(args) > 0:
            return
        for k, v in kwargs.items():
            if k in attrs:
                exec(f"self.{k} = {v}")

    def __str__(self):
        """Print when object is printed."""
        i = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"

    def display(self):
        """Print the rectangle."""
        char = '#'
        print("\n" * self.__y, end="")
        for r in range(self.__height):
            print(' ' * self.__x, end='')
            print(char * self.__width)

    def area(self):
        """Get the area of the rectangle."""
        return self.__width * self.__height

    def validate(name):
        """Validate 'name' before setting it."""
        def decorator(func):
            def wrapper(self, value):
                if not isinstance(value, int):
                    raise TypeError("{:s} must be an integer".format(name))
                if name in ['x', 'y']:
                    if value < 0:
                        raise ValueError("{:s} must be >= 0".format(name))
                else:
                    if value <= 0:
                        raise ValueError("{:s} must be > 0".format(name))
                return func(self, value)
            return wrapper
        return decorator

    @property
    def width(self):
        """Width parameter."""
        return self.__width

    @width.setter
    @validate("width")
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Height parameter."""
        return self.__height

    @height.setter
    @validate("height")
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """For x parameter."""
        return self.__x

    @x.setter
    @validate("x")
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """For y parameter."""
        return self.__y

    @y.setter
    @validate("y")
    def y(self, value):
        self.__y = value
