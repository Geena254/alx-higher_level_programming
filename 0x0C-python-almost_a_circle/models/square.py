#!/usr/bin/python3
"""Module for the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class thar inherits from Rectangle
        Attributes:
            id (int): id of the square
            __width (int): width of the square
            __height (int): height of the square
            __x (int): x position of the square
            __y (int): y position of the square
    """
    # Builtin functions
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of Square
        Arguments:
            size (int): must be >= 0
            x (int): must be > 0
            y (int): must be > 0
            id (int): must be > 0
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        txt = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return txt

    @property
    def size(self):
        """Get the size of square"""
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of the square"""
        self.height = size
        self.width = size
