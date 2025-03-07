import java.util.Scanner;

  public class Exercicio_A1 {

        public static void main (String [] args){

            Scanner att = new Scanner (System.in);

            int  valor1;

            int  valor2; 

                System.out.print("Escreva o primeiro valor de 2: ");
                 valor1 = att.nextInt(); 


                System.out.print("Escreva o segundo valor de 2: ");
                 valor2 = att.nextInt();
    
                if (valor1 > valor2) {

                 System.out.println("primeiro valor é o maior: " + valor1);}

                else {System.out.println("segundo valor é o maior: " + valor2);}
    
            
            att.close();

    }

}