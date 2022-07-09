CREATE DATABASE testdb;
USE testdb;

CREATE TABLE test_table (
    ID int NOT NULL AUTO_INCREMENT,
    sampletext varchar(255),
    PRIMARY KEY(ID)
);

INSERT INTO test_table (sampletext) VALUES ('hello this is a test');
