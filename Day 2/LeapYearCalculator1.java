import java.util.*;

public class Year {
    private int year;

    public Year(int year) {
        this.year = year;
    }

    public int getYear() {
        return year;
    }

    public boolean isLeapYear() {
        if (year % 4 == 0) {
            if (year % 100 != 0) {
                return true;
            } else if (year % 400 == 0) {
                return true;
            }
        }
        return false;
    }
}


public class ValidatedYear extends Year {

    public ValidatedYear(int year) {
        super(year);
    }

    // check for a valid (positive) year
    public boolean isValid() {
        return getYear() > 0;
    }
}

public class LeapYearCalculator1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a year: ");
        int input = scanner.nextInt();

        ValidatedYear yearObj = new ValidatedYear(input);

        if (!yearObj.isValid()) {
            System.out.println("Invalid year. Please enter a positive number.");
        } else {
            if (yearObj.isLeapYear()) {
                System.out.println(input + " is a leap year.");
            } else {
                System.out.println(input + " is not a leap year.");
            }
        }

        scanner.close();
    }
}
