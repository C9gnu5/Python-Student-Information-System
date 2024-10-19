import os

class AddStudent:
    def __init__(self, student_data):
        self.data = student_data
        self.filepath = os.path.dirname(__file__)+"\\"+"students_data.txt"

    def registerLoop(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.input_add_student()
            reg_again = input("Do you want to add another student to the list?(Y/N) ")
            if reg_again.lower() != "y":
                break

    def add_student(self, name, age, idnum, email, phone):
        new = self.data.__class__()
        new.setName(name)
        new.setAge(age)
        new.setIdNum(idnum)
        new.setEmail(email)
        new.setPhone(phone)
        self.data.allstudents.append(new)
        self.write_student(new)
        print(f"Added student {new.getName()} to the list.")

    def input_add_student(self):
        print("="*12,"ADD NEW STUDENT","="*12)
        n, a, i, o, p = input("Enter Name: "), input("Enter Age: "), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone: ")
        print("="*12,"NOTHING FOLLOWS","="*12)
        self.add_student(n, a, i, o, p)
    
    def write_student(self, student):
        with open(self.filepath, 'a+', newline='') as file:
            file.write(f"{student.getName()}, {student.getAge()}, {student.getIdNum()}, {student.getEmail()}, {student.getPhone()}\n")
            file.close()
