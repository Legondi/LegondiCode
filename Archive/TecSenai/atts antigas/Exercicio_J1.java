import java.util.Scanner;

public class Exercicio_J1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int somaIdades = 0;
        int contadorIdades = 0;
        
        while (true) {
            System.out.print("Digite uma idade (ou 0 para encerrar): ");
            int idade = scanner.nextInt();
            
            if (idade == 0) {
                break;  
            }
            
            somaIdades += idade;
            contadorIdades++;
        }
        
        scanner.close();
        
        if (contadorIdades > 0) {
            double mediaIdades = (double) somaIdades / contadorIdades;
            System.out.printf("A média das idades digitadas é: %.2f%n", mediaIdades);
        } else {
            System.out.println("Nenhuma idade foi digitada.");
        }
    }
}