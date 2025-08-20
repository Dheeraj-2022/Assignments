package library;

public class BookFactory {
    public static Book createBook(String type, String title, String author, String isbn, boolean available, int fileSize) {
        if (type.equalsIgnoreCase("ebook")) {
            return new EBook(title, author, isbn, available, fileSize);
        } else {
            return new Book(title, author, isbn, available);
        }
    }
}
