import java.util.Scanner;

public class Exercicio_D1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        int numero;
        do {
            System.out.print("Digite um número de 2 a 10: ");
            numero = scanner.nextInt();
        } while (numero < 2 || numero > 10);

        System.out.println("Tabuada do " + numero + ":");

        for (int i = 1; i <= 10; i++) {
            int resultado = numero * i;
            System.out.println(numero + " x " + i + " = " + resultado);
        }

        scanner.close();
    }
}