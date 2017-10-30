import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SQL {

    public static Connection getDbConnection() {

        try {
            Class.forName("org.sqlite.JDBC");
            Connection connection = DriverManager.getConnection("jdbc:sqlite:database/database");
            System.out.println("Opened database successfully");
            connection.setAutoCommit(false);
            return connection;
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        } return null;
    }

    public static void searchForWord(String word) {
        Statement stmt = null;
        Statement stmt2 = null;
        try (Connection c = getDbConnection()) {
            stmt = c.createStatement();
            stmt2 = c.createStatement();
            ResultSet rs = stmt.executeQuery(
                    "SELECT * FROM customers WHERE name LIKE '%" + word + "%'" +
                            "OR surname LIKE '%" + word + "%'");
            ResultSet rs2 = stmt2.executeQuery(
                    "SELECT * FROM sales WHERE product_name LIKE '%" + word + "%'" +
                            "OR net_value LIKE '%" + word + "%'");
            while ( rs.next() ) {
                int id = rs.getInt("id");
                String firstName = rs.getString("name");
                String lastName = rs.getString("surname");
                String birthYear = rs.getString("birthyear");
                String gender = rs.getString("gender");

                System.out.println("id: " + id);
                System.out.println("first name: " + firstName);
                System.out.println("last name: " + lastName);
                System.out.println("nick name: " + birthYear);
                System.out.println("phone number: " + gender);
                System.out.println();
            }

            while ( rs2.next() ) {
                int id2 = rs2.getInt("id");
                int customerId = rs2.getInt("customer_id");
                String productName = rs2.getString("product_name");
                int netValue = rs2.getInt("net_value");
                int taxRate = rs2.getInt("tax_rate");

                System.out.println("id: " + id2);
                System.out.println("customer id: " + customerId);
                System.out.println("product name: " + productName);
                System.out.println("net value: " + netValue);
                System.out.println("tax rate: " + taxRate);
                System.out.println();
            }
            rs.close();
            rs2.close();
            stmt.close();
            stmt2.close();
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("Operation done successfully");
    }
}
