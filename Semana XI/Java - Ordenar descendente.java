import java.util.Arrays;

public class ArrayTools {
	public static int[] descSorted (int[] array) {
	    int[] newArray = new int[array.length];
	    
	    int colocados = 0;
	    
	    for (int item: array) {
	        int pos = 0;
	        
	        while (pos < colocados && item < newArray[pos]) {
	            pos++;
	        }
	        for (int pos2 = colocados; pos2 > pos; pos2--) {
	            newArray[pos2] = newArray[pos2 - 1];
	        }
	        newArray[pos] = item;
	        colocados++;
	    }
	    return newArray;
	}
	
	public static void main (String[] args) {
	    int[] números = {3, 8, 14, 33, 77, 2};
	    System.out.println(Arrays.toString(descSorted(números)));
	}
}
