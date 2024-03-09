import java.util.Scanner;

class Suma {
    /**
     * main method sums to ints
     */ 
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("Dame un número entero: ");
        int a = input.nextInt();
        System.out.print("Dame otro número entero: ");
        int b = input.nextInt();
        System.out.print(a + b);
        input.close();
    }
}
