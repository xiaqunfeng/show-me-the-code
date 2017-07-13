#!/usr/bin/python3
#import mysql.connector
import pymysql
#import pymysql
#pymysql.install_as_MySQLdb()

def store_mysqldb():
    db = pymysql.connect("localhost", "test", "test123", "testdb")
    #db = mysql.connector.connect("localhost", "testuser", "test123", "TESTDB")
    cursor = db.cursor();
    
    #create a table
    cursor.execute("drop table if exists verify_info")
    sql = """create table verify_info (
        id int not null auto_increment primary key,
        verify_code char(20))"""
    cursor.execute(sql)

    #insert data
    f = open('result.txt', 'r')
    for line in f:
        verify_code = line.strip()
        sql = "insert into verify_info(verify_code) values (%s)" % (verify_code)
        cursor.execute(sql)

    try:
        db.commit()
    except:
        db.rollback()
        f.close()
        print ("error happend when inserting data")
    f.close()
    db.close()

if __name__ == '__main__':
    store_mysqldb()
    
