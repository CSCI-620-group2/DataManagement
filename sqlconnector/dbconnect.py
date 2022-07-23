import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="BigData",
  database="findata"
)





def exec_query_test(query:str) -> dict:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BigData",
        database="findata"
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
