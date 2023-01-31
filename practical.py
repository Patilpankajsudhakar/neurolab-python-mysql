import mysql.connector
import csv 
#import pandas as pd
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute('create database fsds')
# mycursor.execute('use fsds')
# csv_data = csv.reader(open('glass.csv'))
# #print(csv_data)
# csv_data.to_sql=(mycursor,'glass','replace','mysql')
# mydb.commit()
# mycursor.close()
# print("Done")