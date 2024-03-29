/*
ENUNCIADO -->
Añada a la clase ArrayTools un método public static int[] procesar(int[] v1, int[] v2). Los arrays v1 y v2 contienen solo números mayores que cero. El método debe devolver un nuevo array de números enteros cuyo tamaño será igual al del más corto de los dos arrays pasados como parámetros.

Cada posición del nuevo array será:

Si el resto de dividir el valor que ocupa esa posición en v1 por el que ocupa la misma posición en v2 es mayor que 1; se pone el valor de v1.
Si el resto de dividir el valor que ocupa esa posición v1 por el que ocupa la misma posición en v2 es menor o igual que 1; se pone el valor de v2.
Ejemplo:
v1         = [ 1, 3, 5, 9, 2, 8, 8, 5, 8]
v2         = [ 8, 4, 2, 6, 5, 7, 3]
resultado  = [ 8, 3, 2, 9, 2, 7, 8]
-->

----------------------------------------------------------------------------------------------------------------------------------------
MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------MAIN MODULE------
----------------------------------------------------------------------------------------------------------------------------------------
*/
import java.util.Arrays;

public class ArrayTools {
	// Escriba aquí su código
	
}
/*
------------------------------------------------------------------------------------------------------------------------------
SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------SOLUTION MODULE------
------------------------------------------------------------------------------------------------------------------------------
*/
import java.util.Arrays;

public class ArrayTools {
    /** Método que devuelve un nuevo array a partir de otros dos, dependiendo del
     * resto al dividir el elemento del primer array que ocupa la misma posición
     * en el segundo. El nuevo array será de la misma longitud que el más corto.
     */
	public static int[] procesar(int[] v1, int[] v2) {
	    int len = Math.min(v1.length, v2.length);
	    int[] result = new int[len];
	    
	    for (int i = 0; i < len; i++) {
	        result[i] = (v1[i] % v2[i] > 1) ? v1[i]:v2[i];
	    }
	    return result;
	}
}
