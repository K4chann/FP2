import java.util.Scanner;

public class Main {
    public static double km2mi(double km) {
        return km*0.621371;
    }
    
    
    
    public static void main(String[] args) {
         Scanner input = new Scanner(System.in);
         System.out.print("Kilómetros: ");
         double km = input.nextDouble();
         System.out.println("Millas    : " + km2mi(km));
         input.close();
    }
}
