import java.util.Scanner;

public class Main {
    public static void showNumbers(int num1, int num2) {
        for (int i = num1; i <= num2; i++) {
            System.out.println(i);
        }
    }
    
    
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Primer número : ");
        int inf = input.nextInt();
        System.out.print("Segundo número: ");
        int sup = input.nextInt();
        showNumbers(inf, sup);
        input.close();
    }
}
