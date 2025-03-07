import java.util.Scanner;

public class Exercicio_F1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int quantidadePessoas = 10;
        int contadorMaioresDe18 = 0;

        for (int i = 1; i <= quantidadePessoas; i++) {
            System.out.print("Digite a idade da pessoa " + i + ": ");
            int idade = scanner.nextInt();

            if (idade >= 18) {
                contadorMaioresDe18++;
            }
        }

        System.out.println("Quantidade de pessoas com 18 anos ou mais: " + contadorMaioresDe18);

        scanner.close();
    }
}