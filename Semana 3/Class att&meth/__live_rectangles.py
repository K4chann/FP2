"""This module contains the class Rectangle."""


class Rectangle:
    """Quadrilateral with four right angles. Alternate sides are equal."""

    __live_rectangles = 0

    def __init__(self, length, width):
        """Initialize Rectangle objects.

        length: size of the side that we consider the base of the rectangle
        width: size of a side perpendicular to lenght's side

        """
        self.length = length
        self.width = width
        self.__live_rectangles += 1

    @property
    def length(self):
        """Return lenght of self."""
        return self.__length

    @length.setter
    def length(self, value):
        """Update length of self."""
        self.__length = value

    @property
    def width(self):
        """Return width of self."""
        return self.__width

    @width.setter
    def width(self, value):
        """Update width of self."""
        self.__width = value
