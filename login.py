import os

class Login:
    def __init__(self, finder):
        self.finder = finder

    def login(self):
        attempts = 0
        while attempts < 4:
            print("="*10,"Login - Student Info. System","="*10)
            verify = input("\nStudent ID: ")
            user = self.finder.verify_login(verify)
            if user != False:
                return user
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                attempts += 1
                print(f"\nThe student with ID number {verify} does not exit.\nAttempts left: {4 - attempts}")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*10,"Login Error - Student Info. System","="*10+"\nYou have exceeded number of attempts allowed.\nExiting the System. GOODBYE")
        exit()
