
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
    
       
     if (imc < 18.5){ 
        System.out.println("Magresa");
     }  
     
     if (imc > 18.5 & imc < 24.9){ 
        System.out.println("Normal");
     }

      if (imc > 25 & imc < 29.9){ 
        System.out.println("Sobrepeso");
     }

     if (imc > 30 & imc < 34.9){ 
        System.out.println("obesidade grau I");
     }

     if (imc > 35 & imc < 39.9){ 
        System.out.println("obesidade grau II");
     }

     if (imc > 39.9){ 
        System.out.println("obesidade grau III");
     }
     
     else  { 
       
    }
 
}

}
