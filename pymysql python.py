import pymysql

def CreateConn():
    return pymysql.connect(host="localhost",database="project",user="root",password="Aditya@123",port=3306)

# def CreateTable():
#     conn = CreateConn()
#     cursor = conn.cursor()
#     query = "create table AIusers(userid int primary key auto_increment,username varchar(50),email varchar(50),mobile_number int,city varchar(50))"
#     cursor.execute(query)
#     conn.commit()
#     print("Table Created Successfully")
#     conn.close()

def InsertData(username,email,mobile_number,city):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (username,email,mobile_number,city)
    query = "insert into aiusers(username,email,mobile_number,city)values(%s,%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("Data Inserted Successfully")
    conn.close()

username = input("Enter Your Name: ")
email = input("Enter your E-mail: ")
mobile_number = int(input("Enter your mobile Number: "))
city = input("Enter your city name: ")

InsertData(username,email,mobile_number,city)