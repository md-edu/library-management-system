class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books = []  # List to store book IDs of borrowed books
    
    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}"
    
    def borrow_book(self, book_id):
        # To be implemented in Sprint 2
        pass
    
    def return_book(self, book_id):
        # To be implemented in Sprint 2
        pass