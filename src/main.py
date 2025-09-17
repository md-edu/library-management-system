from library import Library
from user import User
from student import Student
from teacher import Teacher
from book import Book

def main():
    library = Library()
    
    # Pre-populate with some data for testing
    library.add_book("B001", "Python Programming", "John Smith", 5)
    library.add_book("B002", "Data Structures", "Jane Doe", 3)
    library.add_book("B003", "Algorithms", "Robert Johnson", 1)

    library.register_user("student", "S001", "Alice Johnson", "pass1", "Computer Science")
    library.borrow_book("S001", "B001")
    library.borrow_book("S001", "B002")
    library.borrow_book("S001", "B003")

    library.register_user("student", "S002", "Bob Smith", "pass2", "Mathematics")
    library.borrow_book("S002", "B001")

    library.register_user("student", "S003", "Charlie Davis", "pass3", "Computer Science")
    library.borrow_book("S003", "B002")

    library.register_user("teacher", "T001", "Dr. Robert Brown", "pass456", "Computer Science")
    
    current_user = None
    
    while True:
        print("\n=== Online Library Management System ===")
        if current_user:
            print(f"Logged in as: {current_user}")
            if isinstance(current_user, Student):
                print("1. View Grades")
                print("2. Request Recommendation")
                print("3. Search Books")
                print("4. Borrow Book")
                print("5. Return Book")
                print("6. View All Books")
                print("7. View My Borrowed Books")
                print("8. Logout")
                print("9. Exit")
            elif isinstance(current_user, Teacher):
                print("1. Add Course Material")
                print("2. Review Student's Borrowed Books")
                print("3. Search Books")
                print("4. Borrow Book")
                print("5. Return Book")
                print("6. View All Books")
                print("7. View My Borrowed Books")
                print("8. Logout")
                print("9. Exit")
            else:
                print("1. Search Books")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. View All Books")
                print("5. View My Borrowed Books")
                print("6. Logout")
                print("7. Exit")
        else:
            print("1. Login")
            print("2. Register")
            print("3. View All Books")
            print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if not current_user:
            if choice == "1":  # Login
                user_id = input("Enter user ID: ")
                password = input("Enter password: ")
                current_user = library.authenticate(user_id, password)
            
            elif choice == "2":  # Register
                user_type = input("Enter user type (student/teacher): ").lower()
                user_id = input("Enter user ID: ")
                name = input("Enter name: ")
                password = input("Enter password: ")
                
                if user_type == "student":
                    major = input("Enter major: ")
                    library.register_user(user_type, user_id, name, password, major)
                elif user_type == "teacher":
                    subject = input("Enter subject: ")
                    library.register_user(user_type, user_id, name, password, subject)
                else:
                    print("Invalid user type!")
            
            elif choice == "3":  # View All Books
                library.display_all_books()
            
            elif choice == "4":  # Exit
                print("Thank you for using the Library Management System!")
                break
            
            else:
                print("Invalid choice! Please try again.")
        
        else:  # User is logged in
            if isinstance(current_user, Student):
                if choice == "1":  # View Grades
                    grades = current_user.view_grades()
                    print("Your grades:")
                    for subject, grade in grades.items():
                        print(f"{subject}: {grade}")
                
                elif choice == "2":  # Request Recommendation
                    recommendation = current_user.request_recommendation()
                    print(f"Recommended book: {recommendation}")
                
                elif choice == "3":  # Search Books
                    title = input("Enter book title to search: ")
                    results = library.search_book(title)
                    if results:
                        print("Search results:")
                        for book in results:
                            print(book)
                    else:
                        print("No books found with that title.")
                
                elif choice == "4":  # Borrow Book
                    library.display_all_books()
                    book_id = input("Enter book ID to borrow: ")
                    library.borrow_book(current_user.user_id, book_id)
                
                elif choice == "5":  # Return Book
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("Books you've borrowed:")
                        for book_id in current_user.borrowed_books:
                            if book_id in library.books:
                                print(library.books[book_id])
                        book_id = input("Enter book ID to return: ")
                        library.return_book(current_user.user_id, book_id)
                
                elif choice == "6":  # View All Books
                    library.display_all_books()
                
                elif choice == "7":  # View My Borrowed Books
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("Books you've borrowed:")
                        for book_id in current_user.borrowed_books:
                            if book_id in library.books:
                                print(library.books[book_id])
                
                elif choice == "8":  # Logout
                    current_user = None
                    print("Logged out successfully!")
                
                elif choice == "9":  # Exit
                    print("Thank you for using the Library Management System!")
                    break
                
                else:
                    print("Invalid choice! Please try again.")
            
            elif isinstance(current_user, Teacher):
                if choice == "1":  # Add Course Material
                    material_name = input("Enter course material name: ")
                    current_user.add_course_material(material_name)
                
                elif choice == "2":  # Review Borrowed Books
                    borrowed_books = current_user.review_borrowed_books(library)
                    print("Borrowed books by students:")
                    for book in borrowed_books:
                        print(book)
                
                elif choice == "3":  # Search Books
                    title = input("Enter book title to search: ")
                    results = library.search_book(title)
                    if results:
                        print("Search results:")
                        for book in results:
                            print(book)
                    else:
                        print("No books found with that title.")
                
                elif choice == "4":  # Borrow Book
                    library.display_all_books()
                    book_id = input("Enter book ID to borrow: ")
                    library.borrow_book(current_user.user_id, book_id)
                
                elif choice == "5":  # Return Book
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("Books you've borrowed:")
                        for book_id in current_user.borrowed_books:
                            if book_id in library.books:
                                print(library.books[book_id])
                        book_id = input("Enter book ID to return: ")
                        library.return_book(current_user.user_id, book_id)
                
                elif choice == "6":  # View All Books
                    library.display_all_books()
                
                elif choice == "7":  # View My Borrowed Books
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("Books you've borrowed:")
                        for book_id in current_user.borrowed_books:
                            if book_id in library.books:
                                print(library.books[book_id])
                
                elif choice == "8":  # Logout
                    current_user = None
                    print("Logged out successfully!")
                
                elif choice == "9":  # Exit
                    print("Thank you for using the Library Management System!")
                    break
                
                else:
                    print("Invalid choice! Please try again.")
            
            else:  # Generic user (shouldn't happen with current implementation)
                if choice == "1":  # Search Books
                    title = input("Enter book title to search: ")
                    results = library.search_book(title)
                    if results:
                        print("Search results:")
                        for book in results:
                            print(book)
                    else:
                        print("No books found with that title.")
                
                elif choice == "2":  # Borrow Book
                    library.display_all_books()
                    book_id = input("Enter book ID to borrow: ")
                    library.borrow_book(current_user.user_id, book_id)
                
                elif choice == "3":  # Return Book
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("Books you've borrowed:")
                        for book_id in current_user.borrowed_books:
                            if book_id in library.books:
                                print(library.books[book_id])
                        book_id = input("Enter book ID to return: ")
                        library.return_book(current_user.user_id, book_id)
                
                elif choice == "4":  # View All Books
                    library.display_all_books()
                
                elif choice == "5":  # View My Borrowed Books
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("Books you've borrowed:")
                        for book_id in current_user.borrowed_books:
                            if book_id in library.books:
                                print(library.books[book_id])
                
                elif choice == "6":  # Logout
                    current_user = None
                    print("Logged out successfully!")
                
                elif choice == "7":  # Exit
                    print("Thank you for using the Library Management System!")
                    break
                
                else:
                    print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()