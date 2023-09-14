import java.math.BigInteger;

public class Exercicio_G {

        public static void main(String[] args) {

            BigInteger contador = BigInteger.valueOf(1);

            for (int i = 1; i <= 64; i++) {    
           
            contador = contador.multiply(BigInteger.valueOf(2));

            System.out.println(contador);
           
            }
            
        }

    }
