import java.util.Scanner;
    
    public class switchh {

        public static void main (String [] args) {

        int teste = 1;
        
        Scanner caso = new Scanner (System.in);

        System.out.println("escolha seu caso de 1 a 3");
        teste = caso.nextInt();

         while (teste < 1 && teste > 4) {

        System.out.println("escolha seu caso de 1 a 3");
        teste = caso.nextInt();
         
         

        switch (teste) {

            case 1:

            System.out.println("voce escolheu Yi");

            break;

            case 2: 

            System.out.println("voce escolheu Er");

            break;

            case 3:
            
            System.out.println("voce escolheu San");

            break;
        }

        

    }
        
    }
    
}