"""This module contains the class Fibonacci, an Iterator."""


class Fibonacci:
    """iterator: Returns, one at a time, the first n Fibonacci numbers."""

    def __init__(self, n):
        """Set the stop condition."""
        if type(n) == int and n > 0:
            self.__n = n
        else:
            raise ValueError(
                "Initalization parameter must be a positive integer"
            )
        self.__current = 0
        self.__next = 1
        self.__counter = 0

    @property
    def n(self):
        """Propiedad del atributo n."""
        return self.__n

    @property
    def next(self):
        """Propiedad del atributo current."""
        return self.__next

    @property
    def current(self):
        """Propiedad del atributo current."""
        return self.__current

    @property
    def counter(self):
        """Propiedad del atributo counter."""
        return self.__counter

    def __iter__(self):
        """Iterador de la clase."""
        return self

    def __next__(self):
        """Método que avanza al siguiente paso de la iteración."""
        if self.counter == self.n:
            raise StopIteration
        else:
            result = self.current
            self.__current, self.__next = self.next, self.current + self.next
            self.__counter += 1
            return result


if __name__ == "__main__":
    for i in Fibonacci(5):
        print(i)
