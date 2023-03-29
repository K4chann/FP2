"""Deletable SortedLinkedList class."""
from sortedlinkedlist import SortedLinkedList


class DeletableSLL(SortedLinkedList):
    """Deletable SortedLinkedList class."""

    def __init__(self):
        """Constructor."""
        super().__init__()

    def delete(self, value):
        """Delete item method."""
        if self._SortedLinkedList__len == 1:
            if self._SortedLinkedList__first.value == value:
                self._SortedLinkedList__first = None
                self._SortedLinkedList__len -= 1
        if self._SortedLinkedList__len > 1:
            prev = self._SortedLinkedList__first
            node = prev.next_node
            while prev is not None and prev.value == value:
                self._SortedLinkedList__first = node
                prev = node
                node = node.next_node if node is not None else None
                self._SortedLinkedList__len -= 1
            while node is not None and node.value <= value:
                if node.value == value:
                    prev.next_node = node.next_node
                    node = node.next_node if node is not None else None
                    self._SortedLinkedList__len -= 1
                else:
                    prev = node
                    node = node.next_node
