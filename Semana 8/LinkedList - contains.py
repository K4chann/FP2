"""Este módulo ofrece una clase para manejar listas encadenadas."""


class LinkedList:
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

    def insert(self, where, value):
        """Inserta un valor por posición en una lista."""
        if where < 0 or where > len(self):
            raise IndexError
        else:
            if where == 0:
                self.__first = self.Node(value, self.__first)
            elif where == len(self):
                new_node = self.Node(value)
                self.__last.next_node = new_node
                self.__last = new_node
            else:
                current = self.__first
                current_pos = 1

                while current_pos < where:
                    current = current.next_node
                    current_pos += 1

                current.next_node = self.Node(value, current.next_node)

            self.__len += 1

    # Escriba su código debajo de esta línea #
    def contains(self, value):
        """Método que busca el elemento pasado en la lista encadenada."""
        current = self.__first

        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        return False
    
if __name__ == "__main__":
    l = LinkedList()
    for num in range(10):
        l.insert(len(l) - 1 if len(l) > 0 else len(l), num)
    
    print(l.contains(10))
