#!/usr/bin/python3
"""Square class representation that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, height is equal to width."""

    def __init__(self, size, x=0, y=0, id=None):
        """Inherit __init__ functionality from super (Rectangle)."""
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """Return dictionary representation of a square."""
        d = {
            'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y
        }
        return d

    def update(self, *args, **kwargs):
        """Set new values for the class instance."""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for n, attr in enumerate(attrs):
                if n >= len(args):
                    break
                if type(args[n]) is str:
                    exec(f"self.{attr} = '{args[n]}'")
                else:
                    exec(f"self.{attr} = {args[n]}")
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    if type(v) is str:
                        exec(f"self.{k} = '{v}'")
                    else:
                        exec(f"self.{k} = {v}")

    def __str__(self):
        """Print square attributes when called in print."""
        i = self.id
        s = self.width
        x = self.x
        y = self.y
        return f"[Square] ({i}) {x}/{y} - {s}"

    @property
    def size(self):
        """Set the value of size."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
