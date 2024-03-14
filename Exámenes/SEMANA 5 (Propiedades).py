"""
ENUNCIADO -->
Se desea crear una clase llamada Rectangulo para representar rectángulos en  un plano de dos dimensiones. Los lados de los rectángulos a representar son paralelos a los ejes x e y. Para representar los rectángulos se parte de los dos puntos que representan su límite inferior izquierdo y el límite superior derecho.

Se dispone, ya desarrollada, de una clase llamada Punto que permite almacenar la coordenada x e y de cada punto (Ver código suministrado para detalles de uso). Usando apropiadamente la clase Punto, desarrolle la clase Rectangulo para que suministren las siguientes características:

El inicializador (constructor) que pasándole dos puntos como parámetros establece el rectángulo a crear. Se pasa como primer parámetro el punto de la esquina inferir izquierda y como segundo el de la esquina derecha superior. En caso de que se pasen puntos que no formen un rectángulo al no ser el de la esquinas correspondientes e, método debe lanzar la excepción BadRectangle establecida en el módulo solution.
perimetro propiedad de solo lectura que representa el perímetro del rectángulo.
superficie propiedad de solo lectura que representa la superficie del rectángulo.
esta_contenido que pasándole un objeto de tipo Punto devuelve si está en el rectángulo o no.
ini propiedad de tipo Punto de lectura y escritura que representa el punto inferior izquierdo. En caso de que se pasé un punto que con el otro no forme un rectángulo se debe lanzar la excepción BadRectangle. 
fin propiedad de tipo Punto de lectura y escritura que representa el punto superior derecho. En caso de que se pasé un punto que con el otro no forme un rectángulo se debe lanzar la excepción BadRectangle.
La representación informal del rectángulo será una ristra en la que aparezcan entre "<" y ">" una representación de los Puntos de las dos esquinas indicadas separados por ", " coma y espacio. Cada punto se representará como los valores de x e y entre paréntesis y separados por ", " coma y espacio:
Ejemplo: para Rectangulo(Punto(1, 2), Punto(3, 4)) se representará como "<(1, 2), (3, 4)>"
Puntos (2, 3) y (3, 4)
Perímetro 4
Superficie 1
Representación <(2, 3), (3, 4)>
Después de escalar 1.5
Perímetro 6.0
Superficie 2.25
Representación <(2, 3), (3.5, 4.5)>
-->

----------------------------------------------------------------------------------------------------------------------------------------
MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------
----------------------------------------------------------------------------------------------------------------------------------------
"""
"""Ejemplo de uso de la funciones requerida."""

from solution import Rectangulo, Punto, BadRectangle
import inspect

tests = [
    (Punto(2, 3), Punto(3, 4)),
    (Punto(-2, 3), Punto(0, 5)),
    (Punto(0, 5), Punto(-2, 6)),
    (Punto(-2, 3), Punto(0, 2)),
]

for p1, p2 in tests:
    try:
        print("Puntos", p1.get_str(), p2.get_str())
        r = Rectangulo(p1, p2)
        print("Perímetro", r.perimetro)
        print("Superficie", r.superficie)
        print("Está contenido el Punto(0, 0)", r.esta_contenido(Punto(0, 0)))
        print("Rectángulo", r)

    except BadRectangle as err:
        print(f"Rectángulo erróneo {p1.get_str()} {p2.get_str()}")
"""
------------------------------------------------------------------------------------------------------------------------------
SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------
------------------------------------------------------------------------------------------------------------------------------
"""
"""Module with the answer to the problem."""

# AÑADA AQUÍ LA CLASE Rectangulo

# NO MODIFIQUE EL CODIGO DEBAJO DE ESTA LINEA


class Punto:
    """Punto con dos propiedades x e y."""

    def __init__(self, x, y):
        """Inicializa punto."""
        self.x = x
        self.y = y

    def get_str(self):
        """Devuelve punto como str."""
        return f"({self.x}, {self.y})"


class BadRectangle(Exception):
    """Exception for BadRectangle."""

    pass
