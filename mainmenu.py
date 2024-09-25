import os

class MainMenu:
    def __init__(self, finder, register, printAll):
        self.finder = finder
        self.register = register
        self.printAll = printAll

    def login(self):
        attempts = 0
        while attempts < 4:
            print("\n"+"="*10,"Login - Student Info. System","="*10)
            verify = input("Student ID: ")
            user = self.finder.verify_login(verify)
            if user != False:
                self.main_menu(user)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                attempts += 1
                print(f"\nThe student with ID number {verify} does not exit.\nAttempts left: {4 - attempts}")
            if attempts > 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n"+"="*10,"Login Error - Student Info. System","="*10+"\nYou have exceeded number of attempts allowed.\nExiting the System. GOODBYE")

    def main_menu(self, user):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome, {user.getName()}!\n"+"="*15,"Main Menu","="*15)
        print("[1] View your information\n[2] View other student's information\n[3] Register a new student\n[4] Print all student in the system\n[5] Exit")
        c = int(input("Your choice: "))
        if c == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*16,"YOUR INFO","="*16+f"\n{user}\n"+"="*13,"NOTHING FOLLOWS","="*13)
            gback = input("\nGo back (Press Enter).")
            if gback == "":
                self.main_menu(user)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*10,"Logging off","="*10+"\nLogging out. GOODBYE")
            exit()
        elif c == 2:
            self.searchStudent()
            self.main_menu(user)
        elif c == 3:
            self.registerStudent()
            self.main_menu(user)
        elif c == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.printAll.printAllStudents()
            gback = input("Go back (Press Enter).")
            if gback == "":
                self.main_menu(user)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*10,"Logging off","="*10+"\nLogging out. GOODBYE")
            exit()
        elif c == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*10,"Logging off","="*10+"\nLogging out. GOODBYE")
            exit()
    
    def searchStudent(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*10,"Search Student Information","="*10)
            id = input("\nEnter student ID Number: ")
            print(self.finder.search_student(id))
            search_again = input("\nDo you want to search again? (Y/N) ")
            if search_again.lower() != "y":
                break
    
    def registerStudent(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.register.input_add_student()
            reg_again = input("Do you want to add another student to the list?(Y/N) ")
            if reg_again.lower() != "y":
                break
