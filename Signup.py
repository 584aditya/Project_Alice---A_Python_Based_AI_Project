from tkinter import *
import pymysql
from tkinter import messagebox


#-------------------------This is the Starting of the section is for the Database Coding--------------------------#


def CreateConn():
    return pymysql.connect(host="localhost",database="project",user="root",password="Aditya@123",port=3306)

def signup():
    n=enm.get()
    e=eem.get()
    p=eps.get()
    m=emn.get()
    c=ect.get()

    if(n=="" or e=="" or p=="" or m=="" or c==""):
        messagebox.showinfo("Error","All Fields are Mandatory")
#-------------------------This is the section for the Database user entry validation--------------------------#
    else:
        try:
            conn=CreateConn()
            cursor=conn.cursor()
            args=(n,e,p,m,c)
            query = "select name,email,password,mobile_number,city from ai_users where name=(%s) and email=(%s) and password=(%s) and mobile_number=(%s) and city=(%s)"
            cursor.execute(query,args)
            dataname=cursor.fetchone()
            if(dataname==None):
                try:
                    conn=CreateConn()
                    cursor=conn.cursor()
                    args=(n,e,p,m,c)
                    query = "insert into ai_users(name,email,password,mobile_number,city)values(%s,%s,%s,%s,%s)"
                    cursor.execute(query,args)
                    conn.commit()
                    messagebox.showinfo("Success!!","Data Inserted Successfuly,Now proceed for Login")
                    conn.close()
                    Clear()
                    switch()
        
                except:
                    messagebox.showinfo("Failure","Data not Inserted")
            else:
                messagebox.showinfo("Error!!","User Already Registered!")
                conn.close()
                Clear()
        
        except:
            messagebox.showinfo("Failure","Data not Inserted")


#-------------------------This is the Ending of the section is for the Database Coding--------------------------#

def switch():
	t.destroy()

t=Tk()

# To change icon of window
photo = PhotoImage(file = "login.png")
t.iconphoto(False,photo)

# To set Window size
t.geometry("400x470")

# Name of the Window
t.title(" Signup Page")

# Background Color for window
t.configure(bg="#333333")

# login page Label
lp = Label(t,text="Signup Page",font=('Arial',30),background="#333333",fg="#fff")
lp.place(x="80",y="15")

# Labels like name,email,password,mobile number,city
nm = Label(t,text="Name",background="#333333",fg="#ff004f",font=('Times',14))
nm.place(x="40",y="96")

em = Label(t,text="E-mail",background="#333333",fg="#ff004f",font=('Times',14))
em.place(x="40",y="156")

ps = Label(t,text="Password",background="#333333",fg="#ff004f",font=('Times',14))
ps.place(x="40",y="216")

mn = Label(t,text="Mobile Number",background="#333333",fg="#ff004f",font=('Times',14))
mn.place(x="40",y="276")

ct = Label(t,text="City",background="#333333",fg="#ff004f",font=('Times',14))
ct.place(x="40",y="336")

# Textfields for the labels
enm=Entry()
enm.place(x="230",y="100")

eem=Entry()
eem.place(x="230",y="160")

eps=Entry(show="*")
eps.place(x="230",y="220")

emn=Entry()
emn.place(x="230",y="280")

ect=Entry()
ect.place(x="230",y="340")

# Function to clear all data in the textfields
def Clear():
    enm.delete(0,END)
    eem.delete(0,END)
    eps.delete(0,END)
    emn.delete(0,END)
    ect.delete(0,END)

# Adding Buttons to window
submit=Button(t,text="Submit",background="#ff004f",width="5",fg="white",height="1",command=signup)
submit.place(x="70",y="410")

reset=Button(t,text="Reset ",background="#ff004f",width="5",fg="white",height="1",command=Clear)
reset.place(x="180",y="410")

login=Button(t,text="Login ",background="#ff004f",fg="white",width="5",height="1",command= switch)
login.place(x="280",y="410")

mainloop()

def Login_Logic():
    username=eem.get()
    password=eps.get()
    if(username=="" or password==""):
        messagebox.showinfo("Error","All Fields are Mandatory")
    else:  
        conn=CreateConn()
        cursor=conn.cursor()
        args=(username,password)
        query="Select email,password from ai_users where email=(%s) and password=(%s)"
        cursor.execute(query,args)
        dataname = cursor.fetchone()
        if(dataname==None):
            messagebox.showinfo("Error!!","Invalid Login")
            eem.delete(0,END)
            eps.delete(0,END)
            # print("Invalid Login")
        else:
            messagebox.showinfo("Success!!","Successfully Logged in")
            


#-------------------------This is the Ending of the section is for the Database Coding--------------------------#


t=Tk()

# To change icon of window
photo = PhotoImage(file = "login.png")
t.iconphoto(False,photo)

# To set Window size
t.geometry("550x350")

# Name of the Window
t.title(" Login page")

# Background Color for window
t.configure(bg="#333333")

# login page Label
lp = Label(t,text="Login Page",font=('Arial',30),background="#333333",fg="#fff")
lp.place(x="180",y="15")

# Labels like name,email,password,mobile number,city

em = Label(t,text="E-mail",background="#333333",fg="#ff004f",font=('Times',14))
em.place(x="100",y="116")

ps = Label(t,text="Password",background="#333333",fg="#ff004f",font=('Times',14))
ps.place(x="100",y="176")

# Textfields for the labels

eem=Entry(width="30")
eem.place(x="300",y="120")

eps=Entry(width="30")
eps.place(x="300",y="180")

# Function to clear all data in the textfields
def Clear():
    eem.delete(0,END)
    eps.delete(0,END)

# Adding Buttons to window
submit=Button(t,text="Submit",background="#ff004f",width="5",fg="white",height="1",command=Login_Logic)
submit.place(x="180",y="280")

reset=Button(t,text="Reset ",background="#ff004f",width="5",fg="white",height="1",command=Clear)
reset.place(x="320",y="280")


# Mainloop so that windows can run continuously
mainloop()
