from user import User
from student import Student

class Teacher(User):
    def __init__(self, user_id, name, password, subject):
        super().__init__(user_id, name, password)
        self.subject = subject
        self.course_materials = []
    
    def __str__(self):
        return f"Teacher - {super().__str__()}, Subject: {self.subject}"
    
    def add_course_material(self, material_name):
        self.course_materials.append(material_name)
        print(f"Added course material '{material_name}' for subject {self.subject}")
        return True
    
    def review_borrowed_books(self, library):
        print(f"Reviewing books borrowed by students for subject {self.subject}")
        
        # Find students who borrowed these books
        borrowed_books_info = []
        for user_id, user in library.users.items():
            if isinstance(user, Student) and user.major.lower() == self.subject.lower():
                for book_id in user.borrowed_books:
                    book = library.books.get(book_id)
                    borrowed_books_info.append({
                            "student": user.name,
                            "book": book.title,
                            "author": book.author
                        })
        
        return borrowed_books_info