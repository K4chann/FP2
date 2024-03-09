import java.util.Arrays;

public class ArrayTools {
	public static int[] listsMaxs (int[] array1, int[] array2) {
	    int[] newArray = new int[
            (array1.length <= array2.length) ?
            array1.length : array2.length
        ];
	    
	    for (int i = 0; i < array1.length; i++) {
	        newArray[i] = (array1[i] > array2[i]) ? array1[i]: array2[i];
	    }
	    return newArray;
	}
	
	public static void main (String[] args) {
	    int[] uno = {3, 8, 14, 33, 77, 2};
	    int[] dos = {12, 34, 7, 16, 16, 89};
	    System.out.println(Arrays.toString(listsMaxs(uno, dos)));
	}
}
