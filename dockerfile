FROM mysql
MAINTAINER CSCI-620 Group 2

LABEL version="1.2"
LABEL description="build mysql server image"

ENV MYSQL_ROOT_PASSWORD BigData
ENV MYSQL_DATABASE finance
ADD database_restore/00-setup.sql /docker-entrypoint-initdb.d
# ADD database_restore/finance_stockprice.sql /docker-entrypoint-initdb.d
# ADD database_restore/backup.sql /docker-entrypoint-initdb.d
# ADD sampleData.sql /docker-entrypoint-initdb.d
# ADD FullDataset.sql /docker-entrypoint-initdb.d

EXPOSE 3306
