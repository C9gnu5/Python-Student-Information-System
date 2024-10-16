import os

class AddStudent:
    def __init__(self, student_data, data_handler):
        self.data = student_data
        self.data_handler = data_handler

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
        self.data_handler.write_student(new)
        print(f"Added student {new.getName()} to the list.")

    def input_add_student(self):
        print("="*12,"ADD NEW STUDENT","="*12)
        n, a, i, o, p = input("Enter Name: "), input("Enter Age: "), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone: ")
        print("="*12,"NOTHING FOLLOWS","="*12)
        self.add_student(n, a, i, o, p)
    