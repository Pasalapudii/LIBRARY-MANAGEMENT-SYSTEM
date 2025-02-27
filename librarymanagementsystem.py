import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #===========================variable=============================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postalcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.latereturnfine = StringVar()
        self.dateoverdue = StringVar()
        self.finalprice = StringVar()

        self.create_database()
    

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="blue", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        #=============================DataFrameLeft==============================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", bd=20, relief=RIDGE,
                                   font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)
        
        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type:", font=("times new roman", 12, "bold"),
                          padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.member_var, width=27,
                                 state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer", "Librarian")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No:", font=("times new roman", 12, "bold"),
                          padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostalCode=Label(DataFrameLeft,bg="powder blue",text="PostalCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostalCode.grid(row=7,column=0,sticky=W)
        txtPostalCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postalcode_var,width=29)
        txtPostalCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,bg="powder blue",text="BookID:",font=("arial",12,"bold"),padx=2)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="DateDue:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverdue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverdue.grid(row=7,column=2,sticky=W)
        txtDateOverdue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue,width=29)
        txtDateOverdue.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice,width=29)
        txtActualPrice.grid(row=8,column=3)

        #===============================DataFrameRight=================================
        DataFrameRight=LabelFrame(frame,text="Book details",bg="powder blue",bd=20,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=580,height=350)

        self.txtBox = Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)


        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook','Intro to Machine Learning','Think Python','Effective Computation in Physics','Learn Python 3 the Hard Way','Python Basics Book','Python for Kids','Teach Your Kids to Code','Python Tricks','Fluent Python',
                 'Effective Python','A Byte of Python','Elements of Programming Interviews in Python','Introduction to Machine Learning with Python','Python for Data Analysis',' Learning Python','Database Programming','Python For EveryBody','Advance Python','Machine Python']

        def SelectBook(event=""):
            selected_indices = listBox.curselection()
            if selected_indices:
                index = selected_indices[0]
                value = listBox.get(index)
                x=value
            if(x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Head First Book")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.788")
            elif(x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID4526")
                self.booktitle_var.set("Learn Python The Hard Way")
                self.author_var.set("ZED A.SHAW")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.725")
            elif(x=="Python Programming"):
                self.bookid_var.set("BKID4326")
                self.booktitle_var.set("Python Programming")
                self.author_var.set("John Zhelle")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.20")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.600")
            elif(x=="Secrete Rahshy"):
                self.bookid_var.set("BKID9856")
                self.booktitle_var.set("Secrete Rahshy")
                self.author_var.set("Ref.Kapil Kamble")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.30")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.800")
            elif(x=="Python CookBook"):
                self.bookid_var.set("BKID2435")
                self.booktitle_var.set("Python CookBook")
                self.author_var.set("Brian Jones")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.40")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.600")
            elif(x=="Intro to Machine Learning"):
                self.bookid_var.set("BKID4325")
                self.booktitle_var.set("Intro to Machine Learning")
                self.author_var.set("Sarah Guaido")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.25")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.500")
            elif(x=="Think Python"):
                self.bookid_var.set("BKID7635")
                self.booktitle_var.set("Think Python")
                self.author_var.set("Allen B. Downey")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.20")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.400")
            elif(x=="Effective Computation in Physics"):
                self.bookid_var.set("BKID9824")
                self.booktitle_var.set("Effective Computation in Physics")
                self.author_var.set("Anthony Scopatz and Kathryn Huff")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.60")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.850")
            elif(x=="Learn Python 3 the Hard Way"):
                self.bookid_var.set("BKID5324")
                self.booktitle_var.set("Learn Python 3 the Hard Way")
                self.author_var.set("Zed A. Shaw")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.45")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.754")
            elif(x=="Python Basics Book"):
                self.bookid_var.set("BKID4523")
                self.booktitle_var.set("Python Basics Book")
                self.author_var.set("Anthony Scopatz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.20")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.200")
            elif(x=="Python for Kids"):
                self.bookid_var.set("BKID9876")
                self.booktitle_var.set("Python for Kids")
                self.author_var.set("Jason Briggs")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.24")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.210")
            elif(x=="Teach Your Kids to Code"):
                self.bookid_var.set("BKID4219")
                self.booktitle_var.set("Teach Your Kids to Code")
                self.author_var.set("Bryson Payne")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.18")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.180")
            elif(x=="Python Tricks"):
                self.bookid_var.set("BKID4386")
                self.booktitle_var.set("Python Tricks")
                self.author_var.set("Dan Bader")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.35")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.350")
            elif(x=="Fluent Python"):
                self.bookid_var.set("BKID7654")
                self.booktitle_var.set("Fluent Python")
                self.author_var.set("Luciano Ramalho")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.35")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.350")
            elif(x=="Effective Python"):
                self.bookid_var.set("BKID3489")
                self.booktitle_var.set("Effective Python")
                self.author_var.set("Brett Slatkin")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.60")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.800")
            elif(x=="A Byte of Python"):
                self.bookid_var.set("BKID6523")
                self.booktitle_var.set("A Byte of Python")
                self.author_var.set("Swaroop")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.45")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.750")
            elif(x=="Elements of Programming Interviews in Python"):
                self.bookid_var.set("BKID6578")
                self.booktitle_var.set("Elements of Programming Interviews in Python")
                self.author_var.set("Adnan Aziz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.60")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.900")
            elif(x=="Introduction to Machine Learning with Python"):
                self.bookid_var.set("BKID5467")
                self.booktitle_var.set("Introduction to Machine Learning with Python")
                self.author_var.set("Andreas Muller")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.45")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.650")
            elif(x=="Python for Data Analysis"):
                self.bookid_var.set("BKID9065")
                self.booktitle_var.set("Python for Data Analysi")
                self.author_var.set("Wes Mckinney")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.40")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.550")
            elif(x=="Learning Python"):
                self.bookid_var.set("BKID9065")
                self.booktitle_var.set("Learning Python")
                self.author_var.set("Mark Lutz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.30")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.450")
            elif(x=="Database Programming"):
                self.bookid_var.set("BKID9065")
                self.booktitle_var.set("Database Programming")
                self.author_var.set("Chris Fehily")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.40")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.550")
            elif(x=="Python For EveryBody"):
                self.bookid_var.set("BKID8765")
                self.booktitle_var.set("Python For EveryBody")
                self.author_var.set("Charles Severance")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.650")
            elif(x=="Advance Python"):
                self.bookid_var.set("BKID9655")
                self.booktitle_var.set("Advance Python")
                self.author_var.set("Dr.Gabriele Lanaro")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.60")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.600")
            elif(x=="Machine Python"):
                self.bookid_var.set("BKID7690")
                self.booktitle_var.set("Machine Python")
                self.author_var.set("Manaranjan Pradhan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine.set("Rs.80")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.800")
            else:
                pass
            
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # ==============================Buttons Frame============================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton,command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue",
                             fg="white")
        btnAddData.grid(row=0, column=1)
        btnAddData=Button(Framebutton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # ==============================Information Frame=========================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, padx=20, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=170)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame,
                                           column=("membertype", "prnno", "id", "firstname", "lastname", "address1",
                                                   "address2", "postalcode", "mobile", "bookid", "booktitle", "author",
                                                   "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue",
                                                   "finalprice"),
                                           xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

         
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("id",text="ID")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postalcode",text="Postal Code")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("id",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postalcode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
    
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)


    def create_database(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS library
                          (membertype TEXT, prnno TEXT, id TEXT, firstname TEXT, lastname TEXT,
                           address1 TEXT, address2 TEXT, postalcode TEXT, mobile TEXT,
                           bookid TEXT, booktitle TEXT, author TEXT, dateborrowed TEXT,
                           datedue TEXT, days TEXT, latereturnfine TEXT, dateoverdue TEXT,
                           finalprice TEXT)''')

        conn.commit()
        conn.close()

    def add_data(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO library (membertype, prnno, id, firstname, lastname, address1, address2, postalcode,
                                                mobile, bookid, booktitle, author, dateborrowed, datedue, days,
                                                latereturnfine, dateoverdue, finalprice)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(),
                        self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(),
                        self.postalcode_var.get(), self.mobile_var.get(), self.bookid_var.get(),
                        self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(),
                        self.datedue_var.get(), self.daysonbook.get(), self.latereturnfine.get(),
                        self.dateoverdue.get(), self.finalprice.get()))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Data Added Successfully!")
    
    def update(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = '''UPDATE library 
        SET membertype=?, prnno=?, id=?, firstname=?, lastname=?, address1=?, address2=?, postalcode=?,
        mobile=?, bookid=?, booktitle=?, author=?, dateborrowed=?, datedue=?, days=?,
        latereturnfine=?, dateoverdue=?, finalprice=?
        WHERE id=?''' 

        values = (self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(),
                    self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(),
                    self.postalcode_var.get(), self.mobile_var.get(), self.bookid_var.get(),
                    self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(),
                    self.datedue_var.get(), self.daysonbook.get(), self.latereturnfine.get(),
                    self.dateoverdue.get(), self.finalprice.get(), self.id_var.get())


        cursor.execute(query, values)
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member updated successfully!")


    def fetch_data(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("Select * from library")
        rows=cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        if cursor_row:
            content = self.library_table.item(cursor_row)
            row = content['values']

            
            self.member_var.set(row[0]),
            self.prn_var.set(row[1]),
            self.id_var.set(row[2]),
            self.firstname_var.set(row[3]),
            self.lastname_var.set(row[4]),
            self.address1_var.set(row[5]),
            self.address2_var.set(row[6]),
            self.postalcode_var.set(row[7]),
            self.mobile_var.set(row[8]),
            self.bookid_var.set(row[9]),
            self.booktitle_var.set(row[10]),
            self.author_var.set(row[11]),
            self.dateborrowed_var.set(row[12]),
            self.datedue_var.set(row[13]),
            self.daysonbook.set(row[14]),
            self.latereturnfine.set(row[15]),
            self.dateoverdue.set(row[16]),
            self.finalprice.set(row[17])


    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Postal Code:\t\t"+ self.postalcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine.get() + "\n")
        self.txtBox.insert(END,"DateOverdue:\t\t"+ self.dateoverdue.get() + "\n")
        self.txtBox.insert(END,"Final Price:\t\t"+ self.finalprice.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postalcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.latereturnfine.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            query="delete from library where prnno=?"
            value=(self.prn_var.get(),)
            cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()


            messagebox.showinfo("Success","Member has been deleted")

root = Tk()
# root.iconbitmap("favicon.ico")
app = LibraryManagementSystem(root)
root.mainloop()
 