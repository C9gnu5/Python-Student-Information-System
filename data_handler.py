import os, csv

class DataHandler:
    def __init__(self, student_data, file='students_data.txt'):
        self.data = student_data
        self.file = os.path.dirname(__file__)+"\\"+file

    def write_student(self, student):
        with open(self.file, 'a', newline='') as f:
            f.write(f"{student.getName()},{student.getAge()},{student.getIdNum()},{student.getEmail()},{student.getPhone()}\n")

    def read_students(self):
        try:
            with open(self.file, 'r') as f:
                reader = csv.reader(f)
                # for line in f:
                for row in reader:
                    name, age, idnum, email, phone = row
                    # name, age, idnum, email, phone = line.strip().split(',')
                    new = self.data.__class__()
                    new.setName(name)
                    new.setAge(age)
                    new.setIdNum(idnum)
                    new.setEmail(email)
                    new.setPhone(phone)
                    self.data.allstudents.append(new)
                    print(f"Added student {new.getName()} to the list.")
        except FileNotFoundError:
            print(f"File {self.file} not found.")
