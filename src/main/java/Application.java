import java.util.Scanner;

public class Application {

    public static String getString() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter searched phrase: ");
        while(scan.hasNextLine()){
            String input = scan.nextLine();
            return input;
        }
        scan.close();
        return null;

    }

    public static void main(String[] args) {
        String order = getString();
        SQL.searchForWord(order);
    }

}
