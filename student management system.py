

def addstudent():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime = time.strftime('%H:%M:%S')
        addeddate = time.strftime('%d/%m/%y')
        try:
           strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
           con.commit()
           res = messagebox.askyesnocancel('Notification','id {} name added sucessfully ... and want to clean the from'.format(id,name),parent=addroot)
           if(res==True):
               idval.set('')
               nameval.set('')
               mobileval.set('')
               emailval.set('')
               addressval.set('')
               genderval.set('')
               dobval.set('')
        except:
            messagebox.showerror('notification','id Already Exist try another id....',parent=addroot)
            strr = 'select * from studentdata'
            mycursor.execute(strr)
            datas = mycursor.fetchall()



    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('student management system')
    addroot.config(bg='blue')
    addroot.iconbitmap('Google-Noto-Emoji-Travel-Places-42496-school.ico')
    addroot.resizable(False,False)
    #-------------------------------------------------------Add Student Labels
    idlabel = Label(addroot,text='Enter Id : ',bg='gold2',font = ('time',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text='Enter name : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    ##------------------------------------------------------------------------------------------------------Add student Entery
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    ##############----------------------------------------Add Button

    submitbn = Button(addroot, text='Submit',font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                      activeforeground='white', bg='red', command=submitadd)
    submitbn.place(x=150, y=420)

    addroot.mainloop()
def serachstudent():
    def search():
        print('search')
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('student management system')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap('Google-Noto-Emoji-Travel-Places-42496-school.ico')
    searchroot.resizable(False,False)
    #-------------------------------------------------------Add Student Labels
    idlabel = Label(searchroot,text='Enter Id : ',bg='gold2',font = ('time',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot, text='Enter name : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    datelabel.place(x=10, y=430)
    ##------------------------------------------------------------------------------------------------------Add student Entery
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    ##############----------------------------------------Add Button

    submitbn = Button(searchroot, text='Submit',font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                      activeforeground='white', bg='red', command=search)
    submitbn.place(x=150, y=480)

    searchroot.mainloop()
def deletestudent():
    print('student delete')
def updatestudent():
    def update():
        print('search')
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('student management system')
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap('Google-Noto-Emoji-Travel-Places-42496-school.ico')
    updateroot.resizable(False,False)
    #-------------------------------------------------------Add Student Labels
    idlabel = Label(updateroot,text='Enter Id : ',bg='gold2',font = ('time',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot, text='Enter name : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time : ', bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    timelabel.place(x=10, y=490)
    ##------------------------------------------------------------------------------------------------------Add student Entery
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    ##############----------------------------------------Add Button

    submitbn = Button(updateroot, text='Submit',font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                      activeforeground='white', bg='red', command=update)
    submitbn.place(x=150,y=540)

    updateroot.mainloop()
def showstudent():
    print('student show')
def exportstudent():
    print('student export')
def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do You Want To Exit')
    if(res==True):
        root.destroy()

######################################################################################connecttion of Database
def connectdb():
    def submitdb():
        #host = hostval.get()
        #user = userval.get()
        #password = passwordval.get()
        host = 'localhost'
        user = 'root'
        password = '12345'
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('notifications','Data is incorrect please try again')
            return
        def addstudent():
            con = pymysql.connect(user="root", host="localhost", password="", database="sms4")
            cur = con.cursor()
            print("okkkkkkk")
        except:

            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('notification','now are you connected to the database .....',parent=dbroot)
            dbroot.destroy()


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x250+500+230")
    dbroot.iconbitmap('Google-Noto-Emoji-Travel-Places-42496-school.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #--------------------------------------------Connectdb  Label
    hostlabel = Label(dbroot,text="Enter Host :",bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User :", bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password :", bg='gold2', font=('time', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    #----------------------------------------------------------Connectedb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    #-----------------------------------------------------------------------------------connectdb button
    submitbutton = Button(dbroot,text='submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()
#########################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d\%m\%y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
################################################################INTRO  SLIDER
import random
colors = ['red','green','yellow','white','blue']
def Introlabelcolortick():
    fg = random.choice(colors)
    sliderLabel.config(fg=fg)
    sliderLabel.after(2,IntroLabelTick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        sliderLabel.config(text=text)
    else:
        text = text+ss[count]
        sliderLabel.config(text=text)
        count += 1
    sliderLabel.after(200,IntroLabelTick)

##############################################################################
from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root = Tk()
root.title('school management system')
root.config(bg='gold2')
root.geometry("1174x690+0+0")
root.iconbitmap('Google-Noto-Emoji-Travel-Places-42496-school.ico')
root.resizable(False,False)
###################################################################################  Frames
##----------------------------------------------------------------------------------dataentry frame

DataEntryFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='------------Welcome----------',width=30,font=('arial',22,'italic bold'),bg='white')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Serach Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=serachstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export Date',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
showDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
showDataFrame.place(x=550,y=80,width=620,height=600)

###############-----------------------------------------------------------------------  Showdataframe
Style = ttk.Style()
Style.configure('Treeview.Heading',font=("chiller",20,'bold'),foreground='blue')
Style.configure('Treeview',font=("time",15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(showDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(showDataFrame,orient=VERTICAL)
studentmttable = Treeview(showDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                          yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studentmttable.xview)
scroll_y.config(command=studentmttable.yview)
studentmttable.heading('Id',text='Id')
studentmttable.heading('Name',text='Name')
studentmttable.heading('Mobile No',text='Mobile No')
studentmttable.heading('Email',text='Email')
studentmttable.heading('Address',text='Address')
studentmttable.heading('Gender',text='Gender')
studentmttable.heading('D.O.B',text='D.O.B')
studentmttable.heading('Added Date',text='Added Date')
studentmttable.heading('Added Time',text='Added Time')
studentmttable['show'] = 'headings'
studentmttable.column('Id',width=100)
studentmttable.column('Name',width=200)
studentmttable.column('Mobile No',width=200)
studentmttable.column('Email',width=300)
studentmttable.column('Address',width=200)
studentmttable.column('Gender',width=100)
studentmttable.column('D.O.B',width=150)
studentmttable.column('Added Date',width=150)
studentmttable.column('Added Time',width=150)

studentmttable.pack(fill=BOTH,expand=1)

####################################################################################  slider
ss = 'welcome to school management system'
count = 0
text = ''
####################################
sliderLabel = Label(root,text=ss,relief=RIDGE,borderwidth=4,font=('chiller',30,'italic bold'),width=35,bg='cyan')
sliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelTick()
#######################################################################  clock
clock = Label(root,relief=RIDGE,borderwidth=4,font=('time',14,'bold'),bg='lawn green')
clock.place(x=0,y=0)
tick()
######################################################################################### ConnectDataButton
connectbutton = Button(root,text='Connect To Database',width=23,relief=RIDGE,font=('chiller',19,'italic bold'),borderwidth=4,bg='green2',activebackground='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()
