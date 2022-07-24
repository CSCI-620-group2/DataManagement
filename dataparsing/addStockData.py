import mysql.connector
import csv
from datetime import datetime

def parseRow(row,colNames,mycursor):
    ep = 0
    colName_insert = []
    colVal_insert = []
    duplicate_insert = []
    for idx, col in enumerate(row):
        
        if idx == 0:
            utc_time =datetime.strptime(col, "%Y-%m-%d %H:%M:%S")
            ep = round((utc_time - datetime(1970, 1, 1)).total_seconds())
        if ((idx - 1) % 5) != 0:
            continue
        colIndex = int((idx - 1) / 5)
        ColName = colNames[colIndex]
        
        if(ep > 0 and len(ColName) > 0 and len(col) > 0):
            colName_insert.append(ColName)
            colVal_insert.append(col)
            duplicate_insert.append(f"{ColName}=VALUES({ColName})")

    if(ep > 0):   
        sqlstring = f"INSERT INTO stockprice (epochtime, {','.join(colName_insert)}) VALUES ({ep},{','.join(colVal_insert)}) ON DUPLICATE KEY UPDATE {','.join(duplicate_insert)};"
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
                newCol = col.replace(".","").replace("ALL","ALLSTATE").replace("KEY","KEYBANK")
                if(newCol != None and len(newCol) > 0 and newCol not in colNames ):
                    colNames.append(newCol)
            rowCount += 1
            continue
        if rowCount < 3:
            rowCount += 1
            continue
        parseRow(row,colNames,mycursor)
        if (idx % 1000 == 0):
            print(idx)
    
mycursor.close()


