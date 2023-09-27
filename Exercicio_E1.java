
public class Exercicio_E1 {
   
    public static void main(String[] args) {
        


     System.out.println("Números entre 1.000 e 2.000 / por 11 produzem resto igual a 2:");

     for (int i  = 1000; i <= 2000; i++) {
        if (( i % 11) == 2) {
            System.out.println(i + " / 11 " + " resta" + (i % 11));
        }
    }
}

}