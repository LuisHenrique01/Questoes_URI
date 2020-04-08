import java.io.IOException;
import java.util.Scanner;
public class Main {
    
    public static void main(String[] args) throws IOException {
        Scanner entrada = new Scanner(System.in);
        double pi, raio, area;
        pi = 3.14159;
        raio = entrada.nextDouble();
        area = pi * Math.pow(raio, 2);
        System.out.printf("A=%.4f\n", area);
    }
 
}