"""Módulo que contiene un iterador llamado PowersOfTwo."""


class PowersOfTwo:
    """Clase iteradora."""

    def __init__(self, stop):
        """Construye los atributos de la clase."""
        self.__start = 0
        self.__stop = stop
        self.__step = 1

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
        """Iterador de la clase."""
        self.__current = self.start
        return self

    def __next__(self):
        """Método que pasa al siguiente paso de la iteración."""
        if self.current < self.stop:
            result = 1 << self.current # Se elige el desplazamiento lógico debido a su eficiencia
            self.__current += self.step
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    for i in PowersOfTwo(7):
        print(i)
