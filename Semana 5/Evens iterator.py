"""Módulo que contiene un iterador."""


class Evens:
    """Clase iteradora."""

    def __init__(self, stop):
        """Construye los atributos de la clase."""
        self.__start = 2
        self.__stop = stop
        self.__step = 2

    @property
    def start(self):
        """Propiedad del atributo start."""
        return self.__start

    @property
    def stop(self):
        """Propiedad del atributo stop."""
        return self.__stop

    @property
    def step(self):
        """Propiedad del atributo step."""
        return self.__step

    @property
    def current(self):
        """Propiedad del atributo current."""
        return self.__current

    def __iter__(self):
        """Método iterador."""
        self.__current = self.__start
        return self

    def __next__(self):
        """Método del siguiente paso del iterador."""
        if self.__current <= self.stop:
            result = self.current
            self.__current += self.__step
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    for i in Evens(10):
        print(i)
