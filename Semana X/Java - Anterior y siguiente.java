import java.util.Scanner;

class Adyacentes {
    /**
     * Muestra los números anterior y posterior a una dado.
     */
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("Dame un número entero: ");
        int num = input.nextInt();
        System.out.println(num - 1);
        System.out.println(num + 1);
        input.close();
    }
}
