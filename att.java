
import java.util.Scanner;
 public class att {

    public static void main(String[] args) {
        
        double peso = 0;
        double altura = 0; 
        double imc = 0;

        Scanner entrada = new Scanner(System.in);

        System.out.println("Seu peso: ");
        peso = entrada.nextDouble();
        System.out.println("Sua Altura: ");
        altura = entrada.nextDouble();

        imc = peso / (altura * altura) ;

        System.out.println("Seu IMC é: ");
        System.out.println(imc);
    }
    
}
