import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb.is_connected())
 
 ## make curser
cur=mydb.cursor()
a=cur.execute('show databases')
a
for x in cur:
  print(x)
