class StudentInfo:
    def __init__(self, name, age, idnum, email, phone):
        self.__name = name
        self.__age = age
        self.__idnum = idnum
        self.__email = email
        self.__phone = phone
        self.__allstudents = []

    def getInfo(self):
        return f"\nName: {self.__name}\nAge: {self.__age}\nID-number: {self.__idnum}\nEmail: {self.__email}\nPhone: {self.__phone}\n"
    
    def getName(self):
        return self.__name
    
    def getIdNum(self):
        return self.__idnum
    
    def getAllStudents(self):
        return self.__allstudents
