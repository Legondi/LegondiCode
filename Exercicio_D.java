import java.util.Scanner;

 public class Exercicio_D {

    public static void main(String [] args) {

     Scanner entrada = new Scanner(System.in);

     int valor = -1;

     int maior = 0;

     int menor = 0;

        while (valor != 0) {
                
        System.out.println("Digite um Numero: ");
       
        valor = entrada.nextInt();

        if (maior < valor){ 
            maior = valor;}

          System.out.println("maior numero é: " + maior);  

        }

    }

}