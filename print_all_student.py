class PrintAllStudent:
    def __init__(self, student_data):
        self.data = student_data

    def printAllStudents(self):
        return f"{'='*17}ALL STUDENT'S INFO{'='*17}\n"+(''.join(f"{student}" for student in self.data.allstudents) if self.data.allstudents else "STUDENT LIST EMPTY.\n")+f"\n{'='*19}NOTHING FOLLOWS{'='*18}\n\n"
