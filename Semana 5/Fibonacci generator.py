"""Módulo que contiene un generador."""


def fibonacci(n):
    """Devuelve los primeros n números de la sucesión de fibonacci."""
    current = 0
    next = 1
    counter = 1

    while counter <= n:
        result = current
        current, next = next, current + next
        yield result
        counter += 1


if __name__ == "__main__":
    for i in fibonacci(5):
        print(i)
