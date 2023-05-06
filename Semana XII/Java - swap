import java.util.Scanner;

public class Functions {
	public static String swap (String text) {
	    String splittedText[] = text.split(" ");
	    String resultText = "";
	    
	    for (String word: splittedText) {
	        String initial = ((Character) word.charAt(0)).toString().toUpperCase();
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
