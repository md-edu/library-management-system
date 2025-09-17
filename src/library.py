from user import User
from student import Student
from teacher import Teacher
from book import Book

class Library:
    def __init__(self):
        self.books = {}  # book_id → Book
        self.users = {}  # user_id → User
        self.passwords = {}  # user_id → password
    
    def add_book(self, book_id, title, author, total_copies):
        if book_id in self.books:
            print("Book ID already exists!")
            return False
        
        self.books[book_id] = Book(book_id, title, author, total_copies)
        print(f"Book '{title}' added successfully!")
        return True
    
    def remove_book(self, book_id):
        if book_id not in self.books:
            print("Book ID does not exist!")
            return False
        
        # Check if any user has borrowed this book
        for user_id, user in self.users.items():
            if book_id in user.borrowed_books:
                print("Cannot remove book. It is currently borrowed by a user!")
                return False
        
        del self.books[book_id]
        print("Book removed successfully!")
        return True
    
    def register_user(self, user_type, user_id, name, password, extra_field):
        if user_id in self.users:
            print("User ID already exists!")
            return False
        
        if user_type == "student":
            self.users[user_id] = Student(user_id, name, password, extra_field)
        elif user_type == "teacher":
            self.users[user_id] = Teacher(user_id, name, password, extra_field)
        else:
            print("Invalid user type!")
            return False
        
        self.passwords[user_id] = password
        print(f"User {name} registered successfully!")
        return True
    
    def authenticate(self, user_id, password):
        if user_id not in self.passwords:
            print("User ID does not exist!")
            return None
        
        if self.passwords[user_id] == password:
            print("Authentication successful!")
            return self.users[user_id]
        else:
            print("Invalid password!")
            return None
    
    def search_book(self, title):
        results = []
        for book_id, book in self.books.items():
            if title.lower() in book.title.lower():
                results.append(book)
        
        return results
    
    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not found!")
            return False
        
        if book_id not in self.books:
            print("Book not found!")
            return False
        
        user = self.users[user_id]
        return user.borrow_book(book_id, self)
    
    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not found!")
            return False
        
        if book_id not in self.books:
            print("Book not found!")
            return False
        
        user = self.users[user_id]
        return user.return_book(book_id, self)
    
    def display_all_books(self):
        if not self.books:
            print("No books in the library!")
            return
        
        print("\n=== All Books in Library ===")
        for book_id, book in self.books.items():
            print(book)