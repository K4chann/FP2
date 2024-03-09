# Este ejercicio ha sido modificado y no dispongo del enunciado original.
# Entiendo que simplemente es eliminar un valor pasado de una SortedLinkedList, debería funcionar bien.
# Si no funciona, les agradecería si me lo hicieran saber por el discord adjunto en la descripción del repositorio.

"""Module which contains a class that inherit from SortedLinkedList."""
from sortedlinkedlist import SortedLinkedList


class DeletableSLL(SortedLinkedList):
    """Class used to delete an element from SortedLinkedList."""

    def __init__(self):
        """Inicializador de la clase."""
        super().__init__()

    def delete(self, value):
        """Método de instancia que elimina el nodo con el valor pasado."""
        # Si la lista tiene sólo un elemento.
        if self._SortedLinkedList__first.value == 0:
            return

        if self._SortedLinkedList__len == 1:
            if self._SortedLinkedList__first.value == value:
                self._SortedLinkedList__first = None
        else:
            prev = self._SortedLinkedList__first
            current = self._SortedLinkedList__first.next_node

            while current is not None and \
                    prev.value != value and \
                    current.value != value:
                prev = prev.next_node
                current = current.next_node
            
            if prev.value == value:
                self._SortedLinkedList__first = current
            else:
                prev.next_node = current.next_node
        
        self._SortedLinkedList__len -= 1
            

