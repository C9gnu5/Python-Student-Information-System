from student import StudentInfo
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from add_student import AddStudent
from mainmenu import MainMenu

stu = StudentInfo()
searcher, addstu, printAll = SearchStudent(stu), AddStudent(stu), PrintAllStudent(stu)
me = MainMenu(searcher, addstu, printAll)

initial_stu = [["Admin Shiiro", "69", "admin", "admin@admin.co", "00009990001"],
        ["Markus", "22", "2023-2-00700", "aurelius@qpal.co", "Eyaw"]]

for i in initial_stu:
    addstu.add_student(*i)

me.login()
