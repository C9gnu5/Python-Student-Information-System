from student import StudentInfo
from search_student import SearchStudent
from mainmenu import MainMenu
from add_student import AddStudent

stu = StudentInfo("name", "age", "idnum", "email", "phone")
searcher = SearchStudent(stu)
adder = AddStudent(stu)
me = MainMenu(searcher, adder)

''' UNCOMMENT THIS SECTION IF YOU WANT TO HAVE AN INITIAL STUDENTS IN THE LIST!!

initial_stu = [["Markus", "22", "2023-2-00700", "aurelius@qpal.co", "Eyaw"],
        ["Joe", "20", "2023-2-00309", "joemama@qpal.co", "Wag pre"],
        ["Joriz", "19", "2023-2-00465", "liampo@qpal.co", "Eeeeyyyy"]]

for i in initial_stu:
    st = StudentInfo(*i)
    register.add_student(st)
'''
me.menu()
