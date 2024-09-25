class StudentInfo:
    def __init__(self):
        self.name, self.age, self.idnum, self.email, self.phone = "", "", "", "", ""
        self.allstudents = []

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
    
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nID-number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}\n"
