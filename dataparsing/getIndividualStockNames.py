import csv

# with open('employee_birthday.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

stockSet = {'BTC','ETH'}

#only one should resolve, regardless it is a set and shouldn't make a difference
oneDot = True
try:
    
    with open('../csvfiles/stockNames.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for col in row:
                stockSet.add(col)
    oneDot = False
except:
    pass

try:
    with open('./csvfiles/stockNames.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for col in row:
                stockSet.add(col.replace(".","").replace("ALL","ALLSTATE").replace("KEY","KEYBANK"))
except:
    pass

stockFileName = "./stock.sql" if oneDot else  "../stock.sql"
f = open(stockFileName, "x")
f.write("CREATE DATABASE finance;\nUSE finance;\n")
f.write("CREATE TABLE stockprice (\nepochtime int UNSIGNED NOT NULL,")

for stock in stockSet:
    f.write(stock + " DECIMAL(20,5),")

f.write("PRIMARY KEY(epochtime)\n);")
f.close()
