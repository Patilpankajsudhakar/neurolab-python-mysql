import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb.is_connected())
 
 ## make curser
cur=mydb.cursor()
#cur.execute("create database fsds_db")
cur.execute("use fsds_db")
cur.execute("create table fsds1(name varchar(50), rollno int, mail_id varchar(50));")