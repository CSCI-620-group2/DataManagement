import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BigData",
    database="finance",
    auth_plugin='mysql_native_password'
)
mydb.autocommit = True
mycursor = mydb.cursor()
idx = 0
with open('./csvfiles/eth.csv', mode='r') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    firstRow = True
    for row in csv_reader:
        idx += 1
        if firstRow or (row[0] == "NaN" or row[1] == "NaN"):
            firstRow = False
            continue
        sqlCommand = f"INSERT INTO stockprice (epochtime,ETH) VALUES ({int(int(row[0]) / 1000)},{row[3]}) ON DUPLICATE KEY UPDATE ETH={row[3]};"
        mycursor.execute("" + sqlCommand)
        #print(sqlCommand)
        if(idx % 1000 == 0):
            print(idx)
mycursor.close()
