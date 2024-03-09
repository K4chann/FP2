import java.util.Scanner;

public class Functions {
	public static String swap (String text) {
	    String splittedText[] = text.split(" ");
	    String resultText = "";

        // Al igual que se explicó en otro ejercicio, es màs eficiente usar StringBuilder.
        // Pero no se volverá a repetir aquí, pueden mirar el ejercicio de la semana XI (Concatenar array)
	    
	    for (String word : splittedText) {
	        String initial = (
                (Character) word.charAt(0)
            ).toString().toUpperCase();
	        resultText = initial + word.substring(1).toLowerCase() + " " + resultText;
	    }
	    return resultText.trim();
	}
	
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Texto a procesar:");
	    String text = input.nextLine();
	    String swapped = swap(text);
	    System.out.print(swapped);
	}
}
