import java.util.Arrays;

public class ArrayTools {
	public static boolean symmetrical (int[][] matrix) {
	    for (int row = 0; row < matrix.length; row++) {
	        for (int column = 0; column < matrix[row].length; column++) {
	            if (matrix[row][column] != matrix[column][row]) {
	                return false;
	            }
	        }
	    }
	    return true;
	}
	
	public static void main (String[] args) {
	    int[][] matriz1 = {
            { 3,  5,  4,  3}, 
            { 5,  7,  5,  8}, 
            { 4,  5,  5,  0},
            { 3,  8,  0,  9},
        }  ;
        System.out.println(symmetrical(matriz1)); // true
	    int[][] matriz2 = {
            { 3,  5,  4,  5}, 
            { 5,  7,  5,  8}, 
            { 9,  5,  5,  0},
            { 3,  8,  0,  9},
        }  ;
        System.out.println(symmetrical(matriz2)); // true
	}
}
