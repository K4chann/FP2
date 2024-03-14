"""
ENUNCIADO -->
Realice las siguientes acciones:

Añada a la clase ColorRGB una variable de clase llamada nombres que sea un diccionario. Las claves del diccionario serán tuplas que representan una combinación rgb y las contraclaves serán strings representando nombres de colores conocidos. Este diccionario estará inicialmente vacío.

Añada a la clase ColorRGB un método de clase establece_nombre(cls, color, nombre), que servirá para añadir un nuevo ítem a la variable de clase nombres. El  parámetro color, que se usará como clave del diccionario nombres, será una tupla de tres números enteros con valores en el rango de 0 a 255, y el parámetro nombre, que se usará como contraclave, será una string.
El método debe asegurarse de que el parámetro color sea una tupla de longitud 3 y que el parámetro nombre sea una string. En caso de no cumplirse la primera condición se lanzará la excepción TypeError con el mensaje "color" y, si se cumple la primera pero no la segunda, se lanzará la excepción TypeError con el mensaje "nombre". No es necesario comprobar que los elementos de la tupla sean de tipo int.

Añada a la clase ColorRGB un propiedad de solo lectura llamada nombre que de el nombre del color representado por el objeto self. Para ello accederá al diccionario nombres usando como clave una tupla formada por la combinación de valores (red, green, blue) del objeto self. En caso de no encontrarse en nombres un ítem con dicha combinación, el método nombre devolverá el valor "desconocido".
-->

----------------------------------------------------------------------------------------------------------------------------------------
MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------
----------------------------------------------------------------------------------------------------------------------------------------
"""
"""Clase a modificar para el ejercicio."""


class ColorRGB:
    """Representa un color en formato RGB."""

    def __init__(self, red, green, blue):
        """Inicializa un objetos con valores para red, green y blue."""
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        """Representación informal colorRGB."""
        color = (self.red, self.green, self. blue)
        return f"{color}"


if __name__ == "__main__":
    c = ColorRGB(0, 0, 0)
    print(c)
    print(c.nombre)

"""
------------------------------------------------------------------------------------------------------------------------------
SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------
------------------------------------------------------------------------------------------------------------------------------
"""
"""Clase a modificar para el ejercicio."""


class ColorRGB:
    """Representa un color en formato RGB."""

    nombres = {}

    def __init__(self, red, green, blue):
        """Inicializa los objetos con valores para red, green y blue."""
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def establece_nombre(cls, color, nombre):
        """Método de clase que añade elementos al diccionario nombres."""
        if type(color) != tuple or len(color) != 3:
            raise TypeError("color")
        elif type(nombre) != str:
            raise TypeError("nombre")
        ColorRGB.nombres[color] = nombre

    @property
    def nombre(self):
        """Propiedad que devuelve el nombre asociado a la clave de color."""
        color = (self.red, self.green, self. blue)
        if color not in ColorRGB.nombres:
            return "desconocido"
        return ColorRGB.nombres[color]

    def __str__(self):
        """Representación informal colorRGB."""
        color = (self.red, self.green, self. blue)
        return f"{color}"


if __name__ == "__main__":
    c = ColorRGB(0, 0, 0)
    print(c)
    print(c.nombre)
