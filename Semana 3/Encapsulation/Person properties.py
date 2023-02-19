"""This module contains the class Person."""


class Person:
    """Represents a person.

    Attributes:
    name   : str the name of a person.
    surname: str the surname of a person.

    """

    def __init__(self, name, surname):
        """Initialize a person Object with name and surname."""
        self.__name = Person.parse(name)
        self.__surname = Person.parse(surname)

    def parse(propiedad):
        """Parse the propierty accrodingly."""
        if (not type(propiedad) == str) or len(propiedad) == 0:
            return 'unknown'
        return propiedad

    @property
    def name(self):
        """Name getter."""
        return self.__name

    @property
    def surname(self):
        """Surname getter."""
        return self.__surname

    @name.setter
    def name(self, name):
        """Surname setter."""
        self.__name = Person.parse(name)

    @surname.setter
    def surname(self, surname):
        """Surname setter."""
        self.__surname = Person.parse(surname)


if __name__ == "__main__":
    # Example of use (not part of the solution)

    person1 = Person(2, "Doe")
    print(f"Name   : {person1.name}")
    print(f"surname: {person1.surname}")
