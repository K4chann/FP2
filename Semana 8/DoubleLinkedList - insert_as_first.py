"""Este módulo ofrece una clase para manejar listas doclemente encadenadas."""


class DoubleLinkedList:
    """Representa una lista doblemente encadenada."""

    class Node:
        """Representaun nodo de una lista doblemente encadenada."""

        def __init__(self, value, prev_node=None, next_node=None):
            """Cada nodo tiene un enlace al anterior y otro al siguiente."""
            self.prev_node = prev_node
            self.value = value
            self.next_node = next_node

    def __init__(self):
        """La lista se inicializa vacía."""
        self.__first = self.__last = None
        self.__len = 0

    def __len__(self):
        """Número de nodos de la lista."""
        return self.__len

    def __iter__(self):
        """Generador para recorrer la lista."""
        current = self.__first

        while current is not None:
            yield current.value
            current = current.next_node

    # Escriba su código debajo de esta línea
    def insert_as_first(self, value):
        """Insert as first mehtod."""
        if self.__first is None:
            self.__first = self.Node(value)
            self.__last = self.__first
        else:
            temp = self.__first
            self.__first = self.Node(value, None, temp)
            temp.prev_node = self.__first
        self.__len += 1
