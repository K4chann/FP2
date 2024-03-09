"""Módulo que contiene un generador."""


def browse_lists(lista1, lista2):
    """Devuelve iterativamente los elementos de una lista y de otra."""

    for index in range(min(len(lista1), len(lista2))):
        yield lista1[index]
        yield lista2[index]


if __name__ == "__main__":
    for i in browse_lists([1, 3, 5, 7, 9], [2, 4, 6]):
        print(i)

    print()

    for i in browse_lists([1, 3, 5, 7], [2, 4, 6, 8, 10, 12]):
        print(i)
