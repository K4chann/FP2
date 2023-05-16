import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Functions {
	public static String verbs (String text) {
	    Pattern pattern = Pattern.compile("(\\w*(o|as|a|amos|áis|an)\\b)");
	    Matcher matcher = pattern.matcher(text);
	    String resultString = "";
	    

	    while (matcher.find()) {
	        resultString += "[" + matcher.group() + "]";
	    }
	    return resultString;
	}
	
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Texto a procesar:");
	    String text = input.nextLine();
	    String verbos = verbs(text);
	    System.out.print(verbos);
	}
}
