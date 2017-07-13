import random
import string

#import mysql.connector
import pymysql

forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        yield Re


def save_code():
    conn = pymysql.connect(user='test', password='test123', database='testdb')
    cursor = conn.cursor()
    codes = generate_code(200, 20)
    for code in codes:
        cursor.execute("INSERT INTO `code`(`code`) VALUES(%s)", params=[code])
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    save_code()
