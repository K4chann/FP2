public class ArrayTools {
    public static int mayores (double[] myArray, double value) {
        int counterGreater = 0;
        
        for (double item: myArray) {
            if (item > value) {
                counterGreater++;
            }
        }
        return counterGreater;
    }
	
	public static void main (String[] args) {
	    double[] arrayOfFloat = {234.5, 1345.24, 500.0, 1455.0, 123.34, 1999.0};
	    System.out.println(mayores(arrayOfFloat, 1000.0));
	}
}
