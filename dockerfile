FROM mysql
MAINTAINER CSCI-620 Group 2

LABEL version="1.0"
LABEL description="build mysql server image"

ENV MYSQL_ROOT_PASSWORD BigData

ADD stock.sql /docker-entrypoint-initdb.d
# ADD sampleData.sql /docker-entrypoint-initdb.d
# ADD FullDataset.sql /docker-entrypoint-initdb.d

EXPOSE 3306
