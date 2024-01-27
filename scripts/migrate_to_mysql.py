

import sqlite3

import pymysql

mysql_con = pymysql.connect(host='localhost', user='root', passwd='root', db='vip', charset='utf8mb4')
sqlite_con = sqlite3.connect('vip.sqlite')

vips = sqlite_con.execute('SELECT * FROM VIP').fetchall()

for vip in vips:
    mysql_con.cursor().execute('INSERT INTO vip  VALUES (%s, %s, %s, %s, %s, %s)', vip)

settings = sqlite_con.execute('SELECT * FROM settings').fetchall()

for setting in settings:
    mysql_con.cursor().execute("INSERT INTO settings VALUES (%s,%s,%s)", setting)

mysql_con.commit()
