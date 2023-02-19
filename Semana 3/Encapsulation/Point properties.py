"""This module contains the class Point."""


class Point:
    """A point in a plane."""

    def __init__(self, x, y):
        """Initialize a point with x and y coordinates."""
        if(not (type(x) == int or type(x) == float)):
            raise TypeError('improper type for x coordinate')
        if(not (type(y) == int or type(y) == float)):
            raise TypeError('improper type for y coordinate')
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """X getter."""
        return self.__x

    @property
    def y(self):
        """Y getter."""
        return self.__y

    @x.setter
    def x(self, x):
        """X setter."""
        if(not (type(x) == int or type(x) == float)):
            raise TypeError('improper type for x coordinate')
        self.__x = x

    @y.setter
    def y(self, y):
        """Y setter."""
        if(not (type(y) == int or type(y) == float)):
            raise TypeError('improper type for y coordinate')
        self.__y = y


if __name__ == "__main__":
    # Example of use (not part of the solution)

    p = Point("6", 4.5)
    print(f"(x = {p.x}, y = {p.y})")
