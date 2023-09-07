 import java.util.Scanner;

 public class maior {

    public static void main(String [] args) {

    double valorA = 0;
     
    double valorB = 0;
      
    double valorC = 0;

      Scanner entrada = new Scanner(System.in);

        System.out.println("Digite o valor A: ");
        valorA = entrada.nextDouble();
       
        System.out.println("Digite o valor B: ");
        valorB = entrada.nextDouble();

        System.out.println("Digite o valor C: ");
        valorC = entrada.nextDouble();

        entrada.close();

            if (valorA > valorB && valorA > valorC){ 
            System.out.println("A");
             } else if (valorB > valorA && valorB > valorC){ 
            System.out.println("B");
             } else if (valorC > valorA && valorC > valorB){ 
            System.out.println("C");
             } else if (valorB == valorA && valorB == valorC){ 
            System.out.println("Todos Iguais");
             }
   
   
    }

    
}
