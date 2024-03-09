public class ArrayTools {
	public static String concatenar (String[] array, String value) {
	    String result = new String();

        // En java existe el StringBuilder, que concatena string eficientemente.
        // Si lo hiciécemos de manera normal, se estaría creando un nuevo objeto string todo el rato.
        // StringBuilder es parecido a meter en una lista en python todo lo que quiera unir y luego hacer "-".join(lista)

        //StringBuilder result = new StringBuilder();
	    
	    for (int i = 0; i < array.length; i++) {
	        result += (i == array.length - 1) ? array[i]: array[i] + value;
            // result.append(array[i]);
            // result.append(value);
	    }
        // if (array.lenth > 0) result.setLength(result.length() - 2);

	    return result;
        //return result.toString();
	}
	
	public static void main (String[] args) {
	    String[] palabras = {"uno", "dos", "tres"};
	    System.out.println(concatenar(palabras,"-")); // "uno-dos-tres"
	}
}
