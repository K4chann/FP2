import java.util.Scanner;

public class Functions {
	public static int initialVowels (String text) {
	    int counter = 0;
	    String vowels = "AEIOUÁÉÍÓÚÜaeiouáéíóúü";
	    String splittedText[] = text.split(" ");
	    
	    if (text.length() > 0) {
	        for (String word: splittedText) {
	                if (vowels.contains(
	                            (
	                                (Character) word.charAt(0)
	                            ).toString()
	                )) {
	                    counter++;
	        	}
	        }
	    }
	    return counter;
	}
	
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Texto a procesar:");
	    String text = input.nextLine();
	    int nVowels = initialVowels(text);
	    System.out.print("El número de palabras que empiezan por vocal es: " + nVowels);
	}
}
