public class aula {
    
public static void main (String [] args){


 int [] [] number = { {2,3,4,},  
                      {1,2,3}, 
                      {7,8,9} };

 for (int i = 0; i < number.length; ++i) {
 for (int j = 0; j < number[i].length; ++j) {
 number [i] [j] = number [i] [j] * 5;

System.out.print(" " + number[i] [j] + " ");

    }

    System.out.println("");

}

}

}
