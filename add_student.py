from student import StudentInfo

class AddStudent:
    def __init__(self, student_data):
        self.data = student_data

    def add_student(self, name, age, idnum, email, phone):
        new = StudentInfo()
        new.setName(name)
        new.setAge(age)
        new.setIdNum(idnum)
        new.setEmail(email)
        new.setPhone(phone)
        self.data.allstudents.append(new)
        print(f"Added student {new.getName()} to the list.")

    def input_add_student(self):
        print("="*12,"ADD NEW STUDENT","="*12)
        n, a, i, o, p = input("Enter Name: "), input("Enter Age: "), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone: ")
        print("="*12,"NOTHING FOLLOWS","="*12)
        self.add_student(n, a, i, o, p)
