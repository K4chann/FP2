"""
ENUNCIADO -->

-->

----------------------------------------------------------------------------------------------------------------------------------------
MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------
----------------------------------------------------------------------------------------------------------------------------------------

There is not a written main module.

------------------------------------------------------------------------------------------------------------------------------
SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------
------------------------------------------------------------------------------------------------------------------------------
"""
"""Módulo que contiene la clase Velero, que hereda de la clase Barco."""

from clases import Barco
from functools import total_ordering


@total_ordering
class Velero(Barco):
    """Clase que hereda de la clase Barco, y representa un tipo de barco."""

    def __init__(self, manga, eslora, palos):
        """Inicializador de la clase Velero."""
        super().__init__(manga, eslora)
        self.palos = palos

    @property
    def palos(self):
        """Propiedad de lectura del atributo palos."""
        return self.__palos

    @palos.setter
    def palos(self, value):
        """Propiedad de escritura del atributo palos."""
        self.__palos = value

    def __eq__(self, other):
        """Comparador de igualdad de las instancias de la clase."""
        if isinstance(other, Barco):
            return (self.manga * self.eslora) == (other.manga * other.eslora)
        return False

    def __lt__(self, other):
        """Comparador menor que de las instancias de la clase."""
        if isinstance(other, Barco):
            return (self.manga * self.eslora) < (other.manga * other.eslora)
        return False
