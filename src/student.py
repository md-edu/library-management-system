from user import User

class Student(User):
    def __init__(self, user_id, name, password, major):
        super().__init__(user_id, name, password)
        self.major = major
    
    def __str__(self):
        return f"Student - {super().__str__()}, Major: {self.major}"
    
    def view_grades(self):
        print(f"Viewing grades for student {self.name}")
        # Simulated grades based on major
        if self.major.lower() == "computer science":
            return {"Programming": "A", "Data Structures": "B+", "Algorithms": "A-", "Database Systems": "B"}
        elif self.major.lower() == "mathematics":
            return {"Calculus": "A", "Linear Algebra": "A-", "Statistics": "B+", "Discrete Math": "A"}
        else:
            return {"Subject 1": "B+", "Subject 2": "A-", "Subject 3": "B", "Subject 4": "A"}
    
    def request_recommendation(self):
        print(f"Book recommendation requested by student {self.name}")
        # Simulated recommendation based on major
        if self.major.lower() == "computer science":
            return "Introduction to Algorithms by Thomas H. Cormen"
        elif self.major.lower() == "mathematics":
            return "Calculus by Michael Spivak"
        elif self.major.lower() == "physics":
            return "The Feynman Lectures on Physics"
        else:
            return "How to Read a Book by Mortimer Adler"