class PrintAllStudent:
    def __init__(self, student_data):
        self.data = student_data

    def printAllStudents(self):
        print("="*15,"ALL STUDENT'S INFO","="*15)
        if len(self.data.allstudents) == 0:
            print("\nSTUDENT LIST EMPTY.\nPLEASE REGISTER A NEW STUDENT FIRST!\n")
        for student in self.data.allstudents:
            print(student)
        print("="*17,"NOTHING FOLLOWS","="*16, "\n\n")
