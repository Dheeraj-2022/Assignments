package library;

import java.util.Scanner;

public class LibraryManager {
    private static LibraryManager instance; // Singleton
    private Library library;
    private Scanner sc;

    private LibraryManager() {
        library = new Library();
        sc = new Scanner(System.in);
    }

    public static LibraryManager getInstance() {
        if (instance == null) {
            instance = new LibraryManager();
        }
        return instance;
    }

    public void showMenu() {
        int choice;
        do {
            System.out.println("\n==== Library Menu ====");
            System.out.println("1. Add Book");
            System.out.println("2. Remove Book");
            System.out.println("3. Search Book");
            System.out.println("4. List Books");
            System.out.println("5. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1 -> addBookMenu();
                case 2 -> removeBookMenu();
                case 3 -> searchBookMenu();
                case 4 -> listBooksMenu();
                case 5 -> System.out.println("Exiting...");
                default -> System.out.println("Invalid choice!");
            }
        } while (choice != 5);
    }

    private void addBookMenu() {
        System.out.print("Enter type (book/ebook): ");
        String type = sc.nextLine();
        System.out.print("Enter title: ");
        String title = sc.nextLine();
        System.out.print("Enter author: ");
        String author = sc.nextLine();
        System.out.print("Enter ISBN: ");
        String isbn = sc.nextLine();
        System.out.print("Is available (true/false): ");
        boolean available = sc.nextBoolean();
        sc.nextLine();

        int fileSize = 0;
        if (type.equalsIgnoreCase("ebook")) {
            System.out.print("Enter file size (MB): ");
            fileSize = sc.nextInt();
            sc.nextLine();
        }

        Book book = BookFactory.createBook(type, title, author, isbn, available, fileSize);
        library.addBook(book);
        System.out.println("Book added!");
    }

    private void removeBookMenu() {
        System.out.print("Enter ISBN to remove: ");
        String isbn = sc.nextLine();
        if (library.removeBook(isbn)) {
            System.out.println("Book removed!");
        } else {
            System.out.println("Book not found!");
        }
    }

    private void searchBookMenu() {
        System.out.print("Enter title to search: ");
        String title = sc.nextLine();
        Book book = library.searchBookByTitle(title);
        System.out.println(book != null ? book : "Book not found!");
    }

    private void listBooksMenu() {
        if (library.listBooks().isEmpty()) {
            System.out.println("No books in library.");
        } else {
            library.listBooks().forEach(System.out::println);
        }
    }
}
