  // Import the File class
import java.io.FileWriter;
import java.io.IOException;  // Import the IOException class to handle errors
import java.util.Random;
import java.time.LocalTime;


public class aula1 {
  public static void main(String[] args) {
   
   
   
    try {
        FileWriter arquivo = new FileWriter ("filename.txt");
         for (int i = 0; i < 100; i++) {
            LocalTime Time = LocalTime.now();
        
            arquivo.append(Time + " " + (int) (Math.random() * 61) + "\n");
        }
        arquivo.close();
        System.out.println("arquivo gravado com sucesso");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}

