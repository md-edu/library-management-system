# librarian.py
from user import User

class Librarian(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)
    
    def __str__(self):
        return f"Librarian - {super().__str__()}"
    
    def add_book(self, library, book_id, title, author, total_copies):
        return library.add_book(book_id, title, author, total_copies)
    
    def remove_book(self, library, book_id):
        return library.remove_book(book_id)
    
    def register_user(self, library, user_type, user_id, name, password, extra_field):
        return library.register_user(user_type, user_id, name, password, extra_field)