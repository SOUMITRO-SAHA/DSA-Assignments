import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();

        // Calling the the findUniqueChar method
        System.out.println(findUniqueChar(s));
    }
    
    // Frequency Map Methods:
    private static int findUniqueChar(String s) {
        HashMap<Character, Integer> fq = new HashMap<>();

        // Filling the fq Array with the frequencies of the Characters in the String
        for (char ch : s.toCharArray()) {
            fq.put(ch, fq.getOrDefault(ch, 0)+1);
        }
        // Finding the first character which has fq 1.
        // If not present, then return -1:
        for (int i = 0; i<s.length(); i++) {
            if(fq.getOrDefault(s.charAt(i), 0) == 1){
                // We found our first unique Character:
                return i;
            }
        }

        return -1;
    }

}
