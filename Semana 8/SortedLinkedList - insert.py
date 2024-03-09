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

    def insert(self, value):
        """Método insert de la lista encadenada."""
        new_node = self.Node(value)

        if self.__first is None:
            self.__first = new_node
        else:
            prev = None
            current = self.__first

            while current is not None and \
                    current.value < value:
                prev = current
                current = current.next_node

            if prev is None:
                self.__first = new_node   
            else:
                prev.next_node = new_node

            new_node.next_node = current

        self.__len += 1

if __name__ == "__main__":
    l = SortedLinkedList()
    for num in range(10):
        l.insert(num)

    for num in l:
        print(num)
    
    l.insert(90)
    l.insert(-5)
    l.insert(-3)

    print("=====================")

    for num in l:
        print(num)

    
