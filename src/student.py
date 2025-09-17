from user import User

class Student(User):
    def __init__(self, user_id, name, password, major):
        super().__init__(user_id, name, password)
        self.major = major
    
    def __str__(self):
        return f"Student - {super().__str__()}, Major: {self.major}"
    
    def view_grades(self):
        # To be implemented in Sprint 3
        print(f"Viewing grades for student {self.name}")
        # Simulated grades
        return {"Math": "A", "Science": "B", "Literature": "A-"}
    
    def request_recommendation(self):
        # To be implemented in Sprint 3
        print(f"Book recommendation requested by student {self.name}")
        # Simulated recommendation
        return "Introduction to Algorithms"