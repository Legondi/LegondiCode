public class string {

    public static void main (String[] args){

       
        // declaração de variavel simples 
        String 你_Nǐ = "Você, ";

        String 在_Zài = "Existir, ";

        String 八_Bā= "8";

        String 五_Wǔ= "5";

        // contagem de caracteres declarados na variavel ex: (variavel.length());
        System.out.println(你_Nǐ.length());

        // coloca as letras em capslock
        System.out.println(你_Nǐ.toUpperCase());

        //coloca as letras em formato "minusculo"
        System.out.println(你_Nǐ.toLowerCase());

        //contabiliza QUALQUER caracter antes da palavra ou letra/numero que voce deseja localizar dentro dos parenteses (OBS: a contagem começa do 0)
        System.out.println(你_Nǐ.indexOf("ê"));

        //alem de usar o operador "+" para concatenar (ligar) as Strings pode ser usado o comando Concat ex: (variavel1.concat(variavel2));
        System.out.println(你_Nǐ.concat(在_Zài));
        //exemplos de concatenação com operador logico
        System.out.println(八_Bā + " " + 五_Wǔ);
        System.out.println(八_Bā + 五_Wǔ);

        //a contra barra "\" pode ser utilizada para usar caraceteres especiais que o java pode "reclamar" caso utilizado em conjunto com outros caracteres especiais em uma string
        System.out.println(你_Nǐ + "\"好_Hǎo = Bom\"");

        System.out.println();


    

    }

}