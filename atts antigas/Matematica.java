public class Matematica {
    

    public static void main(String[] args){

       int 三_Sān = 3;
       
       int 四_Sì = 4;

       int 五_Wǔ = 5;

       int 六_Liù = 6;

       int 十_shí = 10;

       int 七十八_Qīshíbā = 78;

       int 负七_Fù_qī = -7;

       //controla a metrica de aleatoriedade ex: (0 ate 10)
       int random十_shí = (int)(Math.random() * 十_shí);

        System.out.println(random十_shí);



        //mostra o maior valor entre dois parametros (a,b)
        System.out.println(Math.max(三_Sān,四_Sì));

        //mostra o menor valor entre dois parametros (a,b)
        System.out.println(Math.min(五_Wǔ,六_Liù));
        
        //mostra a raiz quadrada de um valor 
        System.out.println(Math.sqrt(七十八_Qīshíbā));

        //transforma o valor negativo em positivo
        System.out.println(Math.abs(负七_Fù_qī));

        //faz qualquer valor aleatorio entre 0.0 e 1.0
        System.out.println(Math.random());

}

}
