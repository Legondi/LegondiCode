import java.util.Scanner;

    public class Exercicio_C1 {
    
        public static void main (String [] args) {

            Scanner att = new Scanner (System.in);

             int x;

             int y;

             int z = 0;

             int w = 0;

            System.out.print("Digite o valor de X: "); 
             x = att.nextInt();

            System.out.print("Digite o valor de Y: "); 
             y = att.nextInt();

            System.out.println("valores de X e Y em respectiva ordem: ");
            System.out.println("X: " + x);
            System.out.println("Y: " + y); 

            if (x != y) {z = x;
                         w = y;
                         x = w;
                         y = z;
                         
             System.out.println("inversão de valores!: " + x);
             System.out.println("inversão de valores!: " + y);}

            else if (x == y){System.out.println("valores iguais: " + y);}             


    
                att.close();
    
        }
    

}
