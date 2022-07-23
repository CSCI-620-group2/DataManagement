import mysql.connector
import csv
from datetime import datetime

def parseRow(row,colNames,mycursor):
    ep = 0
    for idx, col in enumerate(row):
        
        if idx == 0:
            utc_time =datetime.strptime(col, "%Y-%m-%d %H:%M:%S")
            ep = round((utc_time - datetime(1970, 1, 1)).total_seconds())
        if ((idx - 1) % 5) != 0:
            continue
        colIndex = int((idx - 1) / 5)

        ColName = colNames[colIndex]
        if(ep > 0 and len(ColName) > 0 and len(col) > 0):
            sqlstring = f"INSERT INTO stockprice (epochtime, {ColName}) VALUES ({ep},{col}) ON DUPLICATE KEY UPDATE {ColName}={col};"
            mycursor.execute("" + sqlstring)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BigData",
    database="finance",
    auth_plugin='mysql_native_password'
)
mydb.autocommit = True
mycursor = mydb.cursor()

colNames = []
with open('./csvfiles/dataset.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rowCount = 0
    #for row in csv_reader:
    for idx, row in enumerate(csv_reader):
        if rowCount == 0:
            for col in row:
                if(col != None and len(col) > 0 and col not in colNames ):
                    colNames.append(col.replace(".","").replace("ALL","ALLSTATE").replace("KEY","KEYBANK"))
            rowCount += 1
            continue
        if rowCount < 3:
            rowCount += 1
            continue
        parseRow(row,colNames,mycursor)
        if (idx % 10 == 0):
            print(idx)
    
mycursor.close()


