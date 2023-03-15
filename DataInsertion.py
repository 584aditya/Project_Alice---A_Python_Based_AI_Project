import pymysql

def CreateConn():
    return pymysql.connect(host="localhost",database="project",user="root",password="Aditya@123",port=3306)

def InsertData(name,email,password,mobile_number,city):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (name,email,password,mobile_number,city)
    query = "insert into aiusers(name,email,password,mobile_number,city)values(%s,%s,%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("\nData Inserted Successfully")
    conn.close()

n = input("Enter Your Name: ")
e = input("Enter your E-mail: ")
p = input("Enter your Password: ")
m = int(input("Enter your mobile Number: "))
c = input("Enter your city name: ")

InsertData(n,e,p,m,c)