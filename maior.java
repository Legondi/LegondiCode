 import java.util.Scanner;

 public class maior {

    public static void main(String [] args) {

    double valorA = 0;
     
    double valorB = 0;
      
    double valorC = 0;

    int contador = 0;

    while (contador == 0) {
      System.out.println("Numero: " + contador);
      contador++;

      Scanner entrada = new Scanner(System.in);

        System.out.println("Digite o valor A: ");
        valorA = entrada.nextDouble();
       
        System.out.println("Digite o valor B: ");
        valorB = entrada.nextDouble();

        System.out.println("Digite o valor C: ");
        valorC = entrada.nextDouble();

        

            if (valorA > valorB & valorA > valorC){ 
            System.out.println("A é o maior");} 
             
             else if (valorB > valorA & valorB > valorC){ 
            System.out.println("B é o maior");} 
             
             else if (valorC > valorA & valorC > valorB){ 
            System.out.println("C é o maior");}
             
             else if (valorB == valorA | valorB == valorC | (valorC == valorA)){ 
            System.out.println("Valores iguais!!!");
            System.out.println(contador = 0);
          
     }

    

   }

 }

}
