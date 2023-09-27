import java.util.Scanner;

public class Exercicio_G1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int[] faixasEtarias = new int[5]; 
        int totalPessoas = 15;

        for (int i = 0; i < totalPessoas; i++) {
            System.out.print("Digite a idade da pessoa " + (i + 1) + ": ");
            int idade = entrada.nextInt();

            if (idade <= 15) {
                faixasEtarias[0]++; 
            } else if (idade <= 30) {
                faixasEtarias[1]++; 
            } else if (idade <= 45) {
                faixasEtarias[2]++; 
            } else if (idade <= 60) {
                faixasEtarias[3]++; 
            } else {
                faixasEtarias[4]++; 
            }
        }

        System.out.println("Quantidade de pessoas em cada faixa etária:");
        System.out.println("Até 15 anos: " + faixasEtarias[0]);
        System.out.println("De 16 a 30 anos: " + faixasEtarias[1]);
        System.out.println("De 31 a 45 anos: " + faixasEtarias[2]);
        System.out.println("De 46 a 60 anos: " + faixasEtarias[3]);
        System.out.println("Acima de 61 anos: " + faixasEtarias[4]);

        double percentagemPrimeiraFaixa = (faixasEtarias[0] * 100.0) / totalPessoas;
        double percentagemUltimaFaixa = (faixasEtarias[4] * 100.0) / totalPessoas;

        System.out.println("\nPercentagem de pessoas na primeira faixa etária (Até 15 anos): " + percentagemPrimeiraFaixa + "%");
        System.out.println("Percentagem de pessoas na última faixa etária (Acima de 61 anos): " + percentagemUltimaFaixa + "%");

        entrada.close();
    }
}