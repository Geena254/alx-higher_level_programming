#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base


class Rectangle:
    """Represent a rectangle."""

    #class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        # Assign each argument to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        # call the super class with id
        super().__init__()

    # Getter and setter for width
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            ValueError: If value is not an integer or <= 0.
        """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            ValueError: If value is not an integer or <= 0.
        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle.

        Args:
            value (int): The x coordinate value to be set.

        Raises:
            ValueError: If value is not an integer or < 0.
        """
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be greater than 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle.

        Args:
            value (int): The y coordinate value to be set.

        Raises:
            ValueError: If value is not an integer or < 0.
        """
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        if value < 0:
            raise ValueError("y must be greater than 0")
        self.__y = value
