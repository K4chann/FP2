public class ArrayTools {
	public static int divisibles (int[] myArray, int value) {
	    int counter = 0;
	    
	    for (int item: myArray) {
	        if (item % value == 0) {
	            counter++;
	        }
	    }
	    return counter;
	}
	
	public static void main (String[] args) {
	    int[] números = {3, 8, 14, 33, 77, 2};
	    int   divisor = 3;
	    System.out.println(divisibles(números, 3));
	}
}
