"""Módulo que contiene un generador."""


def strings(lista):
    """Generador que devuelve uno por uno los elementos str de una lista."""

    for item in lista:
        if type(item) == str:
            yield item


if __name__ == "__main__":
    for i in strings([5, "uno", 10.8, "dos", 3, 4, "tres", 5]):
        print(i)
