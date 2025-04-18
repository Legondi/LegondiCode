import java.util.Scanner;

    public class Exercicio_B1 {
    
        public static void main(String [] args){

            Scanner att = new Scanner (System.in);

            int idade; 

             System.out.print("Precisamos saber sua idade para aprovar!: ");
              idade = att.nextInt();

            if (idade > 18 && idade < 68) {
             System.out.println("Você atende os requisitos para a doação!");}

            else if (idade < 18) {System.out.print("você é menor de idade");}

            else {System.out.println("você atingiu a idade maxima para a doação");}


        att.close();

    }

}
