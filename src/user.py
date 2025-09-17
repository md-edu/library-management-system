class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books = []  # List to store book IDs of borrowed books
    
    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}"
    
    def borrow_book(self, book_id, library):
        if book_id in self.borrowed_books:
            print("You have already borrowed this book!")
            return False
        
        if book_id not in library.books:
            print("Book not found!")
            return False
        
        book = library.books[book_id]
        if book.available_copies <= 0:
            print("No copies available for borrowing!")
            return False
        
        if book.update_copies(-1):  # Decrease available copies by 1
            self.borrowed_books.append(book_id)
            print(f"Book '{book.title}' borrowed successfully!")
            return True
        else:
            print("Failed to borrow book!")
            return False
    
    def return_book(self, book_id, library):
        if book_id not in self.borrowed_books:
            print("You haven't borrowed this book!")
            return False
        
        if book_id not in library.books:
            print("Book not found in library!")
            return False
        
        book = library.books[book_id]
        if book.update_copies(1):  # Increase available copies by 1
            self.borrowed_books.remove(book_id)
            print(f"Book '{book.title}' returned successfully!")
            return True
        else:
            print("Failed to return book!")
            return False