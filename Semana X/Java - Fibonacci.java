import java.util.Scanner;

public class Functions {
	public static int fibo(int n) {
	    int a = 0;
	    int b = 1;
	    int c;
	    for (int i = 0; i < n; i++) {
	        c = a + b;
	        a = b;
	        b = c;
	    }
	    return a;
	}
	
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.print("Dame un número entero: ");
	    int n = input.nextInt();
	    int f = fibo(n);
	    System.out.print(String.format("El %dº número de Fibonacci es: %d", n, f));
        input.close();
	}
}
