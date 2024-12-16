import os

class SearchStudent:
    def __init__(self, student_data):
        self.data = student_data

    def searchLoop(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*10,"Search Student Information","="*10)
            id = input("\nEnter student ID Number: ")
            print(self.search_student(id))
            search_again = input("\nDo you want to search again? (Y/N) ")
            if search_again.lower() != "y":
                break
    
    def search_student(self, id):
        for student in self.data.allstudents:
            if student.getIdNum() == id:
                print("\nStudent Found: ")
                return f"{'='*16}STUDENT'S INFO{'='*16}\n{student}\n============== NOTHING FOLLOWS =============="
        print(f"\nSTUDENT WITH ID NUMBER {id} NOT FOUND!")
        return False
    
    def verify_login(self, user):
        for student in self.data.allstudents:
            if student.getIdNum() == user:
                return student
        return False
            