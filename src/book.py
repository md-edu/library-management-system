class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available_copies}/{self.total_copies}"
    
    def update_copies(self, change):
        if change > 0:  # Returning a book
            if self.available_copies + change <= self.total_copies:
                self.available_copies += change
                return True
            else:
                return False
        else:  # Borrowing a book
            if self.available_copies >= abs(change):
                self.available_copies -= abs(change)
                return True
            else:
                return False