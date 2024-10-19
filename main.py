from student import StudentInfo
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from add_student import AddStudent
from login import Login
from mainmenu import MainMenu

stu = StudentInfo()
searcher, addstu, printAll = SearchStudent(stu), AddStudent(stu), PrintAllStudent(stu)
login = Login(searcher)
me = MainMenu(searcher, addstu, printAll, login)

me.main_menu()
