// En java.util.Arrays se encuentran métodos que facilitan la tarea de mostrar
// en pantalla el contenido de los arrays
import java.util.Arrays;

public class ArrayTools {
	public static int[] sumLists (int[] array1, int[] array2) {
	    int lenMin = Math.min(array1.length, array2.length);
	    int lenMax = Math.max(array1.length, array2.length);
        int[] supportArray;
	    int[] newArray = new int[lenMax];
	    
	    for (int i = 0; i < lenMin; i++) {
	        newArray[i] = array1[i] + array2[i];
	    }

        supportArray = (array1.length == lenMax) ? array1: array2;

	    for (int i = lenMin; i < lenMax; i++) {
	        newArray[i] = supportArray[i];
	    }
    
	    return newArray;
	}
	
	public static void main (String[] args) {
	    int[] uno = {3, 8, 14, 33, 77, 2};
	    int[] dos = {12, 34, 7, 16};
	    // El método toString de la clase Arrays muestra el contenido
	    // del array devuelto por el método sumLists
	    System.out.println(Arrays.toString(sumLists(uno, dos)));
	}
}
