import java.util.Arrays;

public class ArrayTools {
	public static String[] palabrasEnMente (String[] text) {
	    String result[] = Arrays.copyOf(text, text.length);
	    
	    for (int i = 0; i < result.length; i++) {
	        result[i] = (result[i].contains("mente") && result[i].endsWith("mente")) ?
                result[i].replace("mente", "") : result[i];
	    }
	    return result;
	}

	public static void main (String[] args) {
	    String[] palabras = {"El", "gato", "insolentemente", "saltaba", "ágilmente" };
	    System.out.println(Arrays.toString(palabrasEnMente(palabras)));
	}
}
