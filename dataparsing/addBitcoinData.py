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
 
with open('./csvfiles/bitcoin.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    firstRow = True
    for row in csv_reader:
        if firstRow or (row[0] == "NaN" or row[1] == "NaN"):
            firstRow = False
            continue
        mycursor.execute(f"INSERT INTO stockprice (epochtime,ETH) VALUES ({row[0]},{row[1]}) ON DUPLICATE KEY UPDATE ETH={row[1]};")
        #mycursor.execute(f"INSERT INTO stockprice (epochtime,ETH) VALUES ({row[0]},{row[1]});")


mycursor.close()
