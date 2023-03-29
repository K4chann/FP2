"""Este módulo ofrece una clase para manejar listas encadenadas."""


class SortedLinkedList:
    """Representa una lista simplemente encadenada."""

    class Node:
        """Nodo de una lista simplemente encadenada."""

        def __init__(self, value, next_node=None):
            """Cada nodo tiene un valor y un enlace al siguiente nodo."""
            self.value = value
            self.next_node = next_node

    def __init__(self):
        """Incializa una lista vacía."""
        self.__first = None
        self.__len = 0

    def __len__(self):
        """Devuelve el número de elementos de la lista."""
        return self.__len

    def __iter__(self):
        """Generdor para recorrer la lista."""
        current = self.__first

        while current is not None:
            yield current.value
            current = current.next_node

    def insert(self,  new_value):
        """Insert in correct order."""
        if len(self) == 0:
            self.__first = self.Node(new_value)
        elif self.__first.value >= new_value:
            self.__first = self.Node(new_value, self.__first)
        else:
            prev = self.__first
            current_node = self.__first.next_node
            while current_node is not None and current_node.value < new_value:
                prev = current_node
                current_node = current_node.next_node
            prev.next_node = self.Node(new_value, current_node)
        self.__len += 1
