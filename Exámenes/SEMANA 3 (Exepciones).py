"""Módulo que hace algo."""


def is_upper_triangular_matrix(matrix):
    """Hace algo."""
    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix):
            raise BadMatrix("Matriz no cuadrada")

        for column in range(len(matrix[row])):
            num = matrix[row][column]
            if type(num) != int and type(num) != str:
                raise BadMatrix("Valor no convertible a entero")
            try:
                num = int(num)
            except (ValueError, TypeError):
                raise BadMatrix("Valor no convertible a entero")
            if column < row and num != 0:
                return False
     
    return True

class BadMatrix(Exception):
    pass

m1 = [[1, -1, 2, 3], [0, 4, 0 ,0], [0, 0, -2, 0], [0, 0, 0, -1]] # True
m2 = [[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1]] # True
m3 = [[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1], [0]] # No cuadrada
m4 = [[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0]] # No cuadrada
m5 = [["1", 0, 0], ["0", "44", 1], [0, "-0", "341"]] # True
m6 = [[[], 0, 0], [0, 44, 1], [0, -0, 341]] # BadMatrix, no entero
m7 = [[4, 0, 0], [0, 44, 1], [0, -0, "hola"]] # BadMatrix, no entero

for m in [m1, m2, m3, m4, m5, m6, m7]:
    try:
        print(is_upper_triangular_matrix(m))
    except BadMatrix as err:
        print("Error en matriz", err)
        print(m)
