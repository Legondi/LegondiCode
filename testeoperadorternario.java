public class testeoperadorternario {

    public static void main (String [] args){

        int time = 20;
        String result = (time < 18) ? "Good day." : "Good evening.";
        System.out.println(result);

        int yi = 1;
        int san = (yi < 3) ? 1 + 2 : 3 - 2;
        System.out.println(san);

    }
}