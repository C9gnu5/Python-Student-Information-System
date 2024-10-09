from student import StudentInfo
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from add_student import AddStudent
from data_handler import DataHandler
from mainmenu import MainMenu

stu = StudentInfo()
handler = DataHandler(stu)
searcher, addstu, printAll = SearchStudent(stu), AddStudent(stu, handler), PrintAllStudent(stu)
me = MainMenu(searcher, addstu, printAll)

handler.read_students()

me.login()
