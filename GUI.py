from tkinter import *
import pymysql
from tkinter import messagebox


#-------------------------This is the Starting of the section is for the Database Coding--------------------------#

def CreateConn():
    return pymysql.connect(host="localhost",database="project",user="root",password="Aditya@123",port=3306)

def InsertData():
    n=enm.get()
    e=eem.get()
    p=eps.get()
    m=emn.get()
    c=ect.get()

    if(n=="" or e=="" or p=="" or m=="" or c==""):
        messagebox.showinfo("Error","All Fields are Mandatory")

    else:
        try:
            conn=CreateConn()
            cursor=conn.cursor()
            args=(n,e,p,m,c)
            query = "insert into aiusers(name,email,password,mobile_number,city)values(%s,%s,%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()
            messagebox.showinfo("Success!!","Data Inserted Successfuly,Now proceed for Login")
            conn.close()
        
        except:
            messagebox.showinfo("Failure","Data not Inserted")


#-------------------------This is the Ending of the section is for the Database Coding--------------------------#


t=Tk()

# To change icon of window
photo = PhotoImage(file = "login.png")
t.iconphoto(False,photo)

# To set Window size
t.geometry("400x450")

# Name of the Window
t.title(" Signup Page")

# Background Color for window
t.configure(bg="#afbab7")

# login page Label
lp = Label(t,text="Signup Page",font=('Times',24),background="#afbab7")
lp.place(x="120",y="15")

# Labels like name,email,password,mobile number,city
nm = Label(t,text="Name",background="#afbab7")
nm.place(x="70",y="100")

em = Label(t,text="E-mail",background="#afbab7")
em.place(x="70",y="160")

ps = Label(t,text="Password",background="#afbab7")
ps.place(x="70",y="220")

mn = Label(t,text="Mobile Number",background="#afbab7")
mn.place(x="70",y="280")

ct = Label(t,text="City",background="#afbab7")
ct.place(x="70",y="340")

# Textfields for the labels
enm=Entry()
enm.place(x="210",y="100")

eem=Entry()
eem.place(x="210",y="160")

eps=Entry()
eps.place(x="210",y="220")

emn=Entry()
emn.place(x="210",y="280")

ect=Entry()
ect.place(x="210",y="340")

# Function to clear all data in the textfields
def Clear():
    enm.delete(0,END)
    eem.delete(0,END)
    eps.delete(0,END)
    emn.delete(0,END)
    ect.delete(0,END)

# Adding Buttons to window
submit=Button(t,text="Submit",background="White",width="5",height="1",command=InsertData)
submit.place(x="100",y="400")

reset=Button(t,text="Reset ",background="White",width="5",height="1",command=Clear)
reset.place(x="190",y="400")

login=Button(t,text="Login ",background="White",width="5",height="1")
login.place(x="270",y="400")



# Mainloop so that windows can run continuously
mainloop()
