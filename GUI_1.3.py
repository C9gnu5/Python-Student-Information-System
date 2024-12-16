from student import StudentInfo
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from add_student import AddStudent
from login import Login
from mainmenu import MainMenu
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import pygame
import time

pygame.init()
pygame.mixer.init()

class PyStu:
    def __init__(self):
        self.master = Tk()
        self.dir = os.path.dirname(__file__)

        self.start_it = pygame.mixer.Sound(file=self.dir+"\\sounds\\start.mp3")
        self.shutdown = pygame.mixer.Sound(file=self.dir+"\\sounds\\shutdown.mp3")
        self.start_it.play()

        self.login_frame,self.menu_frame,self.content_frame = LoginFrame(self),MenuFrame(self),ContentFrame(self)
        self.inst_frame,self.myinfo,self.search,self.register,self.pall = InstructionFrame(self),MyInfoFrame(self),SearchFrame(self),RegisterStudent(self),PrintAll(self)

        self.frame_lst = [self.inst_frame,self.myinfo,self.search,self.register,self.pall]

        self.master.title("Python Student Information System"), self.master.config(bg='black')
        self.master.geometry("800x600+"+str((self.master.winfo_screenwidth()//2)-(800//2))+"+"+str((self.master.winfo_screenheight()//2)-(600//2)))
        self.master.mainloop()

    def exit_conf(self):
        confirm = msg.askyesno(title="Are you sure?",message="Are you sure you want to quit the program?")
        if confirm: self.shutdown.play(),time.sleep(2),exit()
    
    def frameForget(self):
        for f in self.frame_lst: f.frame.pack_forget()

    def logoutSwitch(self):
        self.frameForget(),self.menu_frame.frame.place_forget(),self.content_frame.frame.place_forget(),self.search.reset(),self.login_frame.frame.place(relx=0.5,rely=0.5,width=350,height=300,anchor='center')
    
    def loginSwitch(self,user):
        self.login_frame.frame.place_forget(),self.frameForget(),self.menu_frame.set_user(user),self.inst_frame.set_user(user)
        self.menu_frame.frame.place(relx=0.0,rely=0.0,anchor='nw',relwidth=0.06,relheight=1.0),self.content_frame.frame.place(relx=1.0,rely=0.0,anchor='ne',relwidth=0.94,relheight=1.0),self.inst_frame.frame.pack(fill='both', expand=True)

    def myinfoSwitch(self, user):
        self.frameForget(),self.search.reset(),self.myinfo.set_user(user),self.myinfo.frame.pack(fill='both', expand=True)

    def searchSwitch(self):
        self.frameForget(),self.search.txt_s.focus(),self.search.frame.pack(fill='both', expand=True)

    def registerSwitch(self):
        self.frameForget(),self.search.reset(),self.register.frame.pack(fill='both',expand=True),self.register.txt_lst[0].focus()

    def pallSwitch(self):
        self.frameForget(),self.search.reset(),self.pall.frame.pack(fill='both',expand=True)

class LoginFrame:
    def __init__(self,window):
        self.win = window

        self.frame = Frame(self.win.master,borderwidth=1,relief="solid",bg='light grey')
        self.frame.place(relx=0.5,rely=0.5,width=350,height=300,anchor='center')
        Label(self.frame,text="LOG IN",font=("Century Gothic",30,'bold'),foreground='blue',bg='light grey').pack(pady=(20,0))
        self.lbl_err = Label(self.frame,text=f"",font=("Century Gothic",10,'bold'),fg='red',bg='light grey')
        self.lbl_err.place(relx=0.5,rely=0.35,anchor='center')
        Label(self.frame,text="Enter Student ID-Number*",font=("Century Gothic",16,'bold'),bg='light grey').pack(padx=(0,80),pady=(50,0))
        self.usr = Entry(self.frame,font=("Times New Roman",14),border=1,relief='solid')
        self.usr.pack(fill='x',padx=5),self.usr.bind('<Return>',lambda e:self.login()),self.usr.focus()
        Button(self.frame,text="Log In",font=("Century Gothic",16,'bold'),fg='white',background='blue',command=self.login).pack(fill='x',padx=5,pady=(10,0)),Button(self.frame,text="Exit",font=("Century Gothic",16,'bold'),fg='white',background='blue',command=self.win.exit_conf).pack(fill='x',padx=5,pady=(10,0))
        self.a = 0
    
    def login(self):
        user = searcher.verify_login(self.usr.get())
        if user:
            self.usr.delete(0,'end'),self.lbl_err.config(text=f""),self.win.loginSwitch(user)
            self.a = 0
        elif not self.usr.get() or self.usr.get().isspace():
            self.a += 1
            self.lbl_err.config(text=f"Please Enter a Student ID-Number!\nRemaining attempts: {3-self.a}")
        else:
            self.a += 1
            self.lbl_err.config(text=f"Student ID-Number Not Found!\nRemaining attempts: {3-self.a}")
        if self.a == 3:
                msg.showerror(title="Number of Attempts Exceeded",message="You have exceeded the number of attempts!")
                exit()

class MenuFrame:
    def __init__(self,window):
        self.win = window
        self.user = None
        self.dir = window.dir+"\\images\\"
        self.s_dir = window.dir+"\\sounds\\"

        self.frame = Frame(self.win.master,bd=0,bg='light blue')
        self.frame.propagate(False)
        self.frame.bind('<Enter>', self.frame_slide_in),self.frame.bind('<Leave>', self.frame_slide_out)
        self.lbl_usr,self.rights = Label(self.frame,text="UID:",fg='blue',font=('Century Gothic',14,"bold"),bg='light blue'),Label(self.frame,text=" ",fg='blue',font=('Century Gothic',8,"bold"),bg='light blue')
        self.lbl_usr.pack(pady=(25, 25),anchor='w',fill='both'),self.rights.pack(side='bottom',pady=(0,10))
        self.img1,self.img2,self.img3,self.img4,self.img5,self.img6 = ImageTk.PhotoImage(Image.open(f'{self.dir}myinfo.png').resize((40,40))),ImageTk.PhotoImage(Image.open(f'{self.dir}search.png').resize((40,40))),ImageTk.PhotoImage(Image.open(f'{self.dir}register.png').resize((40,40))),ImageTk.PhotoImage(Image.open(f'{self.dir}list.png').resize((40,40))),ImageTk.PhotoImage(Image.open(f'{self.dir}logout.png').resize((40,40))),ImageTk.PhotoImage(Image.open(f'{self.dir}exit.png').resize((40,40)))
        self.btns = [("View Your Information",lambda:self.win.myinfoSwitch(self.user),self.img1),("Search Other Student",self.win.searchSwitch,self.img2),("Register a New Student",self.win.registerSwitch,self.img3),("View All Student",self.win.pallSwitch,self.img4),("Log Out",self.logout,self.img5),("Exit",self.win.exit_conf,self.img6)]
        self.btn_lst,self.selected_btn = [],None
        for t,c,i in self.btns:
            self.btn = Button(self.frame,image=i,compound='left',text=f" ",bg='light blue',bd=0,command=c,font=("Century Gothic",12,'bold'),height=50,anchor='w')
            self.btn.pack(pady=0,fill='x')
            self.btn.bind('<Enter>',self.btn_hover_in),self.btn.bind('<Leave>',self.btn_hover_out),self.btn.bind('<Button-1>',self.on_click),self.btn_lst.append(self.btn)
        self.hover = pygame.mixer.Sound(file=self.s_dir+'hover.mp3')
        self.click = pygame.mixer.Sound(file=self.s_dir+'click.mp3')

    def frame_slide_in(self,event):
        cw,ccw = 0.06,0.94
        while cw < 0.3:
            cw,ccw=cw+0.06,ccw-0.06
            self.frame.place_configure(relwidth=cw)
            self.win.content_frame.frame.place_configure(relwidth=ccw)
            self.win.master.update_idletasks()
        self.lbl_usr.config(text=f"UID: {self.user.getIdNum() if self.user else 'User'}")
        self.rights.config(text="By Python. By tkinter. By C9gnu5.")
        for idx,widget in enumerate(self.frame.winfo_children()):
            if isinstance(widget, Button):
                widget.config(text=f"  {self.btns[idx-2][0]}")

    def frame_slide_out(self,event):
        cw,ccw = 0.3,0.7
        self.lbl_usr.config(text='UID:')
        self.rights.config(text=" ")
        while cw > 0.06:
            cw,ccw=cw-0.06,ccw+0.06
            self.frame.place_configure(relwidth=cw)
            self.win.content_frame.frame.place_configure(relwidth=ccw)
            self.win.master.update_idletasks()
        for widget in self.frame.winfo_children():
            if isinstance(widget, Button):
                widget.config(text=' ')
    
    def btn_hover_in(self,event):
        self.hover.play(0)
        event.widget.config(bg='blue',fg='white')

    def btn_hover_out(self,event):
        if event.widget != self.selected_btn:
            event.widget.config(bg='light blue',fg='black')

    def on_click(self,event):
        self.click.play()
        for btn in self.btn_lst:
            btn.config(bg='light blue',fg='black')
        event.widget.config(bg='blue',fg='white')
        self.selected_btn = event.widget
        if event.widget == self.btn_lst[-2] or event.widget == self.btn_lst[-1]:
            self.selected_btn = None
    
    def set_user(self,user):
        self.user = user
    
    def logout(self):
        confirm = msg.askyesno(title="Log Out",message="Are you sure you want to log out?")
        if confirm:
            self.win.logoutSwitch()
        for btn in self.btn_lst:
            btn.config(bg='light blue',fg='black')

class ContentFrame:
    def __init__(self, window):
        self.win = window
        self.frame = Frame(self.win.master,bg='grey')

class InstructionFrame:
    def __init__(self,window):
        self.win = window
        self.user = None

        self.frame = Frame(self.win.content_frame.frame,bg='white')
        self.lbl = Label(self.frame,text="Welcome User",font=('Century Gothic',16),fg='black',bg='white',justify='left')
        self.lbl.place(relx=0.5,rely=0.5,anchor='center')

    def set_user(self,user):
        self.user = user
        self.lbl.config(text=f"Welcome {self.user.getName()}!\nYou can hover on the sidebar on the right side\nto expand the menu where you can choose to:\n\n  - View your own information\n  - Search other student\n  - Register a new student\n  - View the student list\n  - Log out\n  - Exit")

class MyInfoFrame:
    def __init__(self,window):
        self.win = window
        self.user = None

        self.frame = Frame(self.win.content_frame.frame)
        Label(self.frame,text="Your Information",fg='blue',font=('Century Gothic',24,"bold"),bg="#1ee4bd",height=2).place(anchor='center',relx=0.5,rely=0.2,relwidth=1.0)
        Label(self.frame,text="="*100,font=('Century Gothic',24),fg='blue').place(anchor='center',relx=0.5,rely=0.3),Label(self.frame,text=f"{'='*50}Nothing Follows{'='*50}",font=('Century Gothic',24),fg='blue').place(anchor='center',relx=0.5,rely=0.8)
        self.lbl = Label(self.frame,text="User",font=('Times New Roman',24,'bold'),justify='left')
        self.lbl.place(anchor='center',relx=0.5,rely=0.55)

    def set_user(self,user):
        self.user = user
        self.lbl.config(text=self.user)

class SearchFrame:
    def __init__(self, window):
        self.win = window

        self.frame = Frame(self.win.content_frame.frame)
        Label(self.frame,text="Search a Student",fg='blue',font=('Century Gothic',24,"bold"),bg="#1ee4bd",height=2).place(anchor='center',relx=0.5,rely=0.2,relwidth=1.0)
        self.txt_s = Entry(self.frame,font=("Times New Roman",14),border=1,relief='solid')
        self.txt_s.place(relx=0.15,rely=0.3,anchor='w',relwidth=0.35),self.txt_s.bind('<Return>',lambda e:self.search_stud())
        Button(self.frame,text='Search',font=("Century Gothic",10,'bold'),fg='white',background='blue',command=self.search_stud).place(relx=0.55,rely=0.3,anchor='w',relwidth=0.1),Button(self.frame,text='Clear',font=("Century Gothic",10,'bold'),fg='white',background='blue',command=self.clear).place(relx=0.68,rely=0.3,anchor='w',relwidth=0.1)
        self.lbl_1,self.lbl_2 = Label(self.frame,text=" ",font=('Century Gothic',24),fg='blue'),Label(self.frame,text=" ",font=('Century Gothic',24),fg='blue')
        self.lbl_1.place(anchor='center',relx=0.5,rely=0.38),self.lbl_2.place(anchor='center',relx=0.5,rely=0.88)
        self.lbl = Label(self.frame,text=" ",font=('Times New Roman',24,'bold'),justify='left')
        self.lbl.place(anchor='center',relx=0.5,rely=0.63)

    def search_stud(self):
        stud = searcher.verify_login(self.txt_s.get())
        if stud: self.lbl.config(text=stud),self.clear()
        elif not self.txt_s.get() or self.txt_s.get().isspace(): self.lbl.config(text="Please Enter a Student ID-Number in the Search Box"),self.clear()
        else: self.lbl.config(text=f"No Student with ID-Number '{self.txt_s.get()}' Found!"),self.clear()
        self.lbl_1.config(text="="*100),self.lbl_2.config(text=f"{'='*50}Nothing Follows{'='*50}")

    def clear(self):
        self.txt_s.delete(0,'end')

    def reset(self):
        self.lbl_1.config(text=" "),self.lbl.config(text=" "),self.lbl_2.config(text=" ")

class RegisterStudent:
    def __init__(self, window):
        self.win = window

        self.frame = Frame(self.win.content_frame.frame)
        self.frame.columnconfigure(1, weight=1)
        Label(self.frame,text="Register a Student",fg="blue",font=("Century Gothic", 24, "bold"),bg="#1ee4bd",height=2,).grid(row=0, column=0, columnspan=3, sticky="nsew",pady=(100, 20))
        self.err_lst,self.lbls,self.txt_lst = [Label(self.frame, text=msg, font=("Century Gothic", 10, "bold"), fg="red") for msg in ["NAME REQUIRED!","AGE REQUIRED!","ID-NUMBER REQUIRED!","EMAIL REQUIRED!","PHONE REQUIRED!",]],["Name*", "Age*", "ID-Number*", "Email*", "Phone*"],[]
        for i, lbl_text in enumerate(self.lbls):
            Label(self.frame,text=lbl_text,font=("Century Gothic", 14, "bold"),).grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)
            entry = Entry(self.frame, font=("Times New Roman", 14), border=1, relief="solid")
            entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=5)
            self.txt_lst.append(entry)
        self.btn = Button(self.frame,text="Clear",font=("Century Gothic", 12, "bold"),fg="white",bg="blue",width=15,command=self.clear_form)
        self.btn.grid(row=len(self.lbls) + 1, column=0, pady=(20, 10),padx=(15,0))
        self.btn = Button(self.frame,text="Register",font=("Century Gothic", 12, "bold"),fg="white",bg="blue",width=15,command=self.submit_add)
        self.btn.grid(row=len(self.lbls) + 1, column=1,columnspan=2, pady=(20, 10),padx=(0,15),sticky='e')

    def submit_add(self):
        error_shown = False
        for i, err_label in enumerate(self.err_lst):
            if not self.txt_lst[i].get():
                err_label.grid(row=i + 1, column=2, sticky="w", padx=10)
                error_shown = True
            else: err_label.grid_forget()
        if not error_shown:
            name, age, idnum, email, phone = [entry.get() for entry in self.txt_lst]
            addstu.add_student(name,age,idnum,email,phone)
            msg.showinfo(title="Student Added", message=f"Added student {name} to the list!")
            self.clear_form()

    def clear_form(self):
        for entry in self.txt_lst: entry.delete(0, END)
        for err in self.err_lst: err.grid_forget()
        self.txt_lst[0].focus()

class PrintAll:
    def __init__(self,window):
        self.win = window
        self.dir = window.dir+"\\images\\"

        self.re_img = ImageTk.PhotoImage(Image.open(f'{self.dir}refresh.png').resize((25,25)))

        self.frame = Frame(self.win.content_frame.frame)
        Label(self.frame,text="View All Student",fg='blue',font=('Century Gothic',24,"bold"),bg="#1ee4bd",height=2).place(anchor='center',relx=0.5,rely=0.2,relwidth=1.0)
        self.table = ttk.Treeview(self.frame,column=("name","age","idnum","email","phone"),show='headings')
        self.table.place(relx=0.5,rely=0.6,anchor='center',relwidth=0.95,relheight=0.5)
        self.table.heading("name",text="Name"),self.table.heading("age",text="Age"),self.table.heading("idnum",text="ID-Number"),self.table.heading("email",text="Email"),self.table.heading("phone",text="Phone")
        self.table.column("name",width=30,anchor='center'),self.table.column("age",width=5,anchor='center'),self.table.column("idnum",width=50,anchor='center'),self.table.column("email",width=50,anchor='center'),self.table.column("phone",width=100,anchor='center')
        self.scrollbar = Scrollbar(self.frame,orient='vertical',command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.99,rely=0.5,anchor='center',relheight=1.0)
        Button(self.frame,image=self.re_img,compound='left',text='',bd=0,bg='light grey',command=self.add_data).place(relx=0.05,rely=0.31,anchor='center')
        self.existing_ids = set()

        self.add_data()

    def add_data(self):
        self.table.delete(*self.table.get_children())
        self.existing_ids.clear() 
        for stud in stu.allstudents:
            if stud.getIdNum() not in self.existing_ids:
                data = (stud.getName(),stud.getAge(),stud.getIdNum(),stud.getEmail(),stud.getPhone())
                self.table.insert('',index='end',values=data)
                self.existing_ids.add(stud.getIdNum())

stu = StudentInfo()
searcher,addstu,printAll = SearchStudent(stu),AddStudent(stu),PrintAllStudent(stu)
login = Login(searcher)
me = MainMenu(searcher,addstu,printAll,login)

PyStu()
