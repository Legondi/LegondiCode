 import java.util.Scanner;

 public class maior {

    public static void main(String [] args) {

    double valorA = 0;
     
    double valorB = 0;
      
    double valorC = 0;

    int contador = 0;

      Scanner entrada = new Scanner(System.in);

      while (contador == 0) {
        contador++;


        System.out.print("Digite o valor A: ");
        valorA = entrada.nextDouble();
       
        System.out.print("Digite o valor B: ");
        valorB = entrada.nextDouble();

        System.out.print("Digite o valor C: ");
        valorC = entrada.nextDouble();

        

            if (valorA > valorB & valorA > valorC){ 
            System.out.println("A é o maior");} 
             
             else if (valorB > valorA & valorB > valorC){ 
            System.out.println("B é o maior");} 
             
             else if (valorC > valorA & valorC > valorB){ 
            System.out.println("C é o maior");}
             
             else if (valorB == valorA | valorB == valorC | (valorC == valorA)){ 
            System.out.println("Valores iguais!!!");
            contador = 0;
          
     }

   }

   entrada.close();

 }

}
