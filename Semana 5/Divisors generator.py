"""Módulo que contiene un generador."""


def divisors(stop):
    """Generador de divisores de un entero positivo."""
    for num in range(1, stop + 1):
        if stop % num == 0:
            yield num


if __name__ == "__main__":
    for div in divisors(12):
        print(div)
