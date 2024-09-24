from student import StudentInfo

class AddStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def add_student(self):
        print("\n============ADD NEW STUDENT=============")
        n, a, i, o, p = input("\nEnter Name: "), input("Enter Age: "), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone: ")
        print("\n============NOTHING FOLLOWS=============\n")
        s = StudentInfo(n, a, i, o, p)
        self.student_data.getAllStudents().append(s)
        print(f"Added student {s.getName()} to the list.")