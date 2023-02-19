"""This module contains the class Time."""


class Time:
    """Represents a time."""

    def __init__(self, h, m):
        """Initialize Time objects hours and minutes."""
        self.hour = h
        self.minute = m

    def __repr__(self):
        """Formal representation."""
        return f'Time({self.hour}, {self.minute})'

    def __str__(self):
        """Informal representation."""
        return f'{self.hour:02}:{self.minute:02}'


if __name__ == "__main__":
    # Example of use (not part of the solution)

    t = Time(12, 5)
    print("Formal: {}".format(repr(t)))
    print("Informal: {}".format(t))
