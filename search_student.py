class SearchStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def search_student(self, id):
        for student in self.student_data.getAllStudents():
            if student.getIdNum() == id:
                print("\n============STUDENT'S INFO============\n")
                print(student.getInfo()) 
                return "\n============NOTHING FOLLOWS==========="
        return f"\nSTUDENT WITH ID NUMBER {id} COULD NOT BE FOUND!"
            
    def printAllStudentInfo(self):
        print("\n============ALL STUDENT'S INFO============\n")
        if len(self.student_data.getAllStudents()) == 0:
            print("STUDENT LIST EMPTY.\nPLEASE REGISTER A NEW STUDENT FIRST!")
        for student in self.student_data.getAllStudents():
            print(student.getInfo())
        print("\n==============NOTHING FOLLOWS=============")
        