class SearchStudent:
    def __init__(self, student_data):
        self.data = student_data

    def search_student(self, id):
        for student in self.data.allstudents:
            if student.getIdNum() == id:
                print("\nStudent Found: ")
                print("="*16,"STUDENT'S INFO","="*16)
                print(student) 
                return "================ NOTHING FOLLOWS ==============="
        return f"\nSTUDENT WITH ID NUMBER {id} NOT FOUND!"
    
    def verify_login(self, user):
        for student in self.data.allstudents:
            if student.getIdNum() == user:
                return student
        return False
            