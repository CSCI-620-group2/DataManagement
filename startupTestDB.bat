del containerid.cid
del stock.sql
python ./dataparsing/getIndividualStockNames.py
docker build -t stockdatabase .
docker run --cidfile "containerid.cid" -dp 3306:3306 stockdatabase 

