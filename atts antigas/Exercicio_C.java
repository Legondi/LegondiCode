import java.util.Scanner;
 public class Exercicio_C {

        public static void main(String[] args) {

            Scanner entrada = new Scanner(System.in);

            int valor;

            valor = entrada.nextInt();
           
                while (valor != 0 && valor != 1) {
                
                System.out.println("Digite 1 ou 0: ");
               
                valor = entrada.nextInt();     

        }

      entrada.close();

    }

}
