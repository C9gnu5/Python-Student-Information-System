import os

class StudentInfo:
    def __init__(self):
        self.name, self.age, self.idnum, self.email, self.phone = "", "", "", "", ""
        self.allstudents = []
        self.filepath = os.path.dirname(__file__)+"\\"+"students_data.txt"

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIdNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phone):
        self.phone = phone
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getIdNum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def readData(self):
        try:
            with open(self.filepath, 'r') as file:
                rows = file.readlines()
                for line in rows:
                    name, age, idnum, email, phone = line.split(",")
                    new = self.__class__()
                    new.setName(name.strip())
                    new.setAge(age.strip())
                    new.setIdNum(idnum.strip())
                    new.setEmail(email.strip())
                    new.setPhone(phone.strip())
                    self.allstudents.append(new)
                    print(f"Added student {new.getName()} to the list.")
        except FileNotFoundError:
            print(f"File not found.")
    
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nID-number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}\n"
