# library.py
from user import User
from student import Student
from teacher import Teacher

class Library:
    def __init__(self):
        self.books = {}  # book_id → Book
        self.users = {}  # user_id → User
        self.passwords = {}  # user_id → password
    
    def add_book(self, book_id, title, author, total_copies):
        if book_id in self.books:
            print("Book ID already exists!")
            return False
        
        self.books[book_id] = [book_id, title, author, total_copies]
        print(f"Book '{title}' added successfully!")
        return True
    
    def remove_book(self, book_id):
        if book_id not in self.books:
            print("Book ID does not exist!")
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
        # To be implemented in Sprint 2
        pass
    
    def borrow_book(self, user_id, book_id):
        # To be implemented in Sprint 2
        pass
    
    def return_book(self, user_id, book_id):
        # To be implemented in Sprint 2
        pass