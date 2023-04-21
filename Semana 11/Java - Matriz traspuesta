import java.util.Arrays;

public class ArrayTools {
	public static int[][] transpose (int[][] matrix) {
	    int[][] newMatrix = new int[matrix[0].length][matrix.length];
	    for (int row = 0; row < matrix.length; row++) {
	        for (int column = 0; column < matrix[0].length; column++) {
	            newMatrix[column][row] = matrix[row][column];
	        }
	    }
	    return newMatrix;
	}
	
	public static void main (String[] args) {
	    int[][] matriz1 = {
            { 3,  5,  4,  3}, 
            { 5,  7,  5,  8}, 
            { 4,  5,  5,  0},
        };
        int[][] result = transpose(matriz1);
        
        for (int i = 0; i < result.length; i++) {
            System.out.println(Arrays.toString(result[i]));
        }
	}
}
