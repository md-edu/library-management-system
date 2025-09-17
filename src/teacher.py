from user import User

class Teacher(User):
    def __init__(self, user_id, name, password, subject):
        super().__init__(user_id, name, password)
        self.subject = subject
    
    def __str__(self):
        return f"Teacher - {super().__str__()}, Subject: {self.subject}"
    
    def add_course_material(self, material_name):
        # To be implemented in Sprint 3
        print(f"Added course material '{material_name}' for subject {self.subject}")
        return True
    
    def review_borrowed_books(self, library):
        # To be implemented in Sprint 3
        print(f"Reviewing books borrowed by students for subject {self.subject}")
        # This will be implemented in Sprint 3
        return []