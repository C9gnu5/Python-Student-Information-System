import os
# from student import StudentInfo

class MainMenu:
    def __init__(self, finder, register):
        self.finder = finder
        self.register = register

    def menu(self):
        m = int(input("""
Welcome, Admin Shiiro! 
Please choose any of the following:
[1] View your information
[2] View other student's information
[3] Register a New Student
[4] Print all students in the list
[5] Exit
                      
Enter your choice: """))
        if m == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nTHIS FEATURE IS STILL UNDER DEVELOPMENT!!")
            self.backToMenu()
        elif m == 2: self.searchStudent()
        elif m == 3: self.registerStudent()
        elif m == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.finder.printAllStudentInfo()
            self.backToMenu()
        elif m == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n!!INVALID CHOICE!!")
            self.menu()

    def backToMenu(self):
        back = input("\nPress 'Y' to go back to Main Menu or any key to quit program: ")
        if back.lower() != 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.menu()
    
    def searchStudent(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            id = input("\nEnter student ID Number: ")
            print(self.finder.search_student(id))
            search_again = input("\nDo you want to search again? (Y/N) ")
            if search_again.lower() != "y":
                self.backToMenu()
    
    def registerStudent(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.register.add_student()
            reg_again = input("\nDo you want to add another student to the list?(Y/N) ")
            if reg_again.lower() != "y":
                self.backToMenu()
