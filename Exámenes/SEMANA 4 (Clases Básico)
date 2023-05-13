ENUNCIADO -->
Se desea crear una clase llamada Matriz para representar objetos de tipo matriz. Los métodos que suministrarán los objetos de esta clase serán los siguientes:

El constructor que pasándole una lista de listas como datos de la matriz posibilitará inicializar un objeto.
es_cuadrada que devolverá verdadero si la matriz tiene el mismo número de filas que de columnas en todas sus filas.
nfilas que devolverá el número de filas de la matriz.
ncolumnas que devolverá el número máximo de columnas en las filas de la matriz
get_str devuelve una ristra que representa la matriz de forma que si se imprime la ristra la matriz se muestre en líneas. Cada línea será el resultado de la función str de cada fila de la matriz.
Ejemplo:

Para la matriz [[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1], [0]]
es_cuadrada => False
nfilas => 5
ncolumnas => 4
get_str => [1, 0, 0, 0]
[0, 4, 0, 0]
[0, 0, -2, 0]
[0, 0, 0, -1]
[0]
-->

----------------------------------------------------------------------------------------------------------------------------------------
MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------
----------------------------------------------------------------------------------------------------------------------------------------

"""Ejemplo de uso de la función requerida."""

from solution import Matriz

ms = []
ms.append([[1, 1], [0, 0]])
# Descomente líneas para probar más casos
# ms.append([[1, -1, 2, 3], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1]])
# ms.append([[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1]])
# ms.append([[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, -1], [0]])
# ms.append([[1, 0, 0, 0], [0, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0]])
# ms.append([["1", 0, 0], ["0", "44", 1], [0, "-0", "341"]])
# ms.append([[[], 0, 0], [0, 44, 1], [0, -0, 341]])
# ms.append([[4, 0, 0], [0, 44, 1], [0, -0, "hola"]])

for i, m in enumerate(ms):
    mat = Matriz(m)
    print(f"===== MATRIZ {i+1} =====")
    print("es_cuadrada", mat.es_cuadrada())
    print("nfilas", mat.nfilas())
    print("ncolumnas", mat.ncolumnas())
    print("Representación ", mat.get_str())
    
------------------------------------------------------------------------------------------------------------------------------
SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------
------------------------------------------------------------------------------------------------------------------------------

"""Module with the answer to the problem."""

from copy import deepcopy


class Matriz:
    """Clase que representa objetos de tipo matriz."""

    def __init__(self, matrix: list):
        """Contructor de la clase Matriz."""
        self.matrix = deepcopy(matrix)

    def es_cuadrada(self):
        """Método de instancia que devuelve True si la matriz es cuadrada."""
        for row in self.matrix:
            if len(row) != len(self.matrix):
                return False
        return True

    def nfilas(self):
        """Método de instancia que devuelve el número de filas de la matriz."""
        return len(self.matrix)

    def ncolumnas(self):
        """Método de instancia que devuelve la columna de máxima longitud."""
        return max([len(row) for row in self.matrix])

    def get_str(self):
        """Método que devuelve una fila de la matriz por línea como string."""
        return "\n".join([str(row) for row in self.matrix])
