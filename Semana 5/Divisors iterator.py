"""This module contains the class Divisors which is an Iterator."""


class Divisors:
    """iterator: Returns, one at a time, the divisors os a positive integer."""

    def __init__(self, number):
        """Set number to get its Divisors.

        raise ValueError is number is not a positive integer.
        """
        if type(number) == int and number > 0:
            self.__number = number
        else:
            raise ValueError(
                "Initalization parameter must be a positive integer"
                )
        self.__start = 0
        self.__step = 1
        self.__steps = [i for i in range(1, number + 1) if number % i == 0]

    @property
    def number(self):
        """Propiedad del atributo number."""
        return self.__number

    @property
    def start(self):
        """Propiedad del atributo start."""
        return self.__start

    @property
    def step(self):
        """Propiedad del atributo step."""
        return self.__step

    @property
    def steps(self):
        """Propiedad del atributo steps."""
        return self.__steps

    @property
    def current(self):
        """Propiedad del atributo current."""
        return self.__current

    def __iter__(self):
        """Iterador de la clase."""
        self.__current = self.start
        return self

    def __next__(self):
        """Método que avanza al siguiente paso del iterador."""
        if self.current <= (len(self.steps) - 1):
            result = self.steps[self.current]
            self.__current += self.__step
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    for i in Divisors(12):
        print(i)
