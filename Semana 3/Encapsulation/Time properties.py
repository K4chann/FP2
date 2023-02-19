"""This module contains the class Time."""


class Time:
    """Represents a time."""

    def __init__(self, h, m):
        """Initialize Time objects with hours and minutes."""
        self.__hour = self.check_hours(h)
        self.__minute = self.check_minutes(m)

    def check_hours(self, h):
        """Check that the hours provided are coherent."""
        if not (type(h) == int) or h < 0:
            return 0
        elif h > 23:
            return 23
        else:
            return h

    def check_minutes(self, m):
        """Check that the minutes provided are coherent."""
        if not (type(m) == int) or m < 0:
            return 0
        elif m > 59:
            return 59
        else:
            return m

    @property
    def hour(self):
        """Hour getter."""
        return self.__hour

    @property
    def minute(self):
        """Minute getter."""
        return self.__minute

    @hour.setter
    def hour(self, h):
        """Hour setter."""
        self.__hour = self.check_hours(h)

    @minute.setter
    def minute(self, m):
        """Minute setter."""
        self.__minute = self.check_minutes(m)


if __name__ == "__main__":
    # Example of use (not part of the solution)

    t = Time("12", 5)
    print(t.hour)
    print(f"{t.hour:02}:{t.minute:02}")
