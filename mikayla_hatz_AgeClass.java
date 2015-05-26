import java.util.Scanner;

public class Age
{

    
    public static void main(String[] args)
    { 
        Scanner user_input = new Scanner(System.in);
        
        System.out.print("What month were you born in? (1 = January, 2 = February, etc.): ");
        double month = user_input.nextDouble();
        System.out.print("How old are you?: ");
        double age = user_input.nextDouble();
        
     
          
        double specialNumber = (2 * month + 5) * 50 + age - 365;
        System.out.print("Special number is: " + specialNumber); 
        specialNumber = specialNumber + 115;
        double newAge = specialNumber % 100; 
        System.out.print("");
        double newMonth = (specialNumber - newAge) / 100; 
        System.out.print(newAge); 
        System.out.print(newMonth); 
        
        
        
       /*printing out stuff */
        System.out.print("\nIt is calculated that you were born in the " + newMonth + " month and are " + newAge + " years old.\n");
        
   
    
    
