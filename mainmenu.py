import os

class MainMenu:
    def __init__(self, finder, register, printAll, login):
        self.finder = finder
        self.register = register
        self.printAll = printAll
        self.login = login
    

    def main_menu(self):
        user = self.login.login()
        a = 0
        while a < 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Welcome, {user.getName()}!\n"+"="*15,"Main Menu","="*15)
            print("[1] View your information\n[2] View other student's information\n[3] Register a new student\n\
[4] Print all student in the system\n[5] Logout\n[6] Exit")
            c = int(input("Your choice: "))
            if c == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*16,"YOUR INFO","="*16+f"\n{user}\n"+"="*13,"NOTHING FOLLOWS","="*13)
                gback = input("\nGo back (Press Enter).")
                if gback == "":
                    continue
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*10,"Logging off","="*10+"\nLogging out. GOODBYE")
                exit()
            elif c == 2:
                self.finder.searchLoop()
            elif c == 3:
                self.register.registerLoop()
            elif c == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.printAll.printAllStudents())
                gback = input("Go back (Press Enter).")
                if gback == "":
                    continue
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*10,"Logging off","="*10+"\nExiting the System. GOODBYE")
                exit()
            elif c == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main_menu()
            elif c == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*10,"Logging off","="*10+"\nExiting the System. GOODBYE")
                exit()
            else:
                a += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*10,"Error - Student Info. System","="*10+"\nYou seem to be trolling by deliberately not choosing within the choices.\nExiting the System. GOODBYE")
        exit()
    