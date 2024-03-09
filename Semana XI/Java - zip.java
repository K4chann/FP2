import java.util.Arrays;

public class ArrayTools {
	public static int[][] zip(int[] array1, int[] array2) {
        int[][] result = new int[Math.min(array1.length, array2.length)][2];
	    
	    for (int row = 0; row < result.length; row++) {
	        result[row][0] = array1[row];
            result[row][1] = array2[row];
	    }
	    
	    return result;
	}
	
	public static void main (String[] args) {
	    int[] uno = {3, 8, 14, 33, 77, 2};
	    int[] dos = {12, 34, 7, 16};
	    int[][] tres = zip(uno, dos);
	    
	    for (int i = 0; i < tres.length; i++) {
	        System.out.println(Arrays.toString(tres[i]));
	    }
	}
}
