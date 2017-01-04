#! /usr/bin/env python
# coding: utf-8

# 操作数据库
__author__ = 'Tallulah Yang'

import pymysql

conn = pymysql.connect(user='root', host='localhost', db='test')
cur = conn.cursor()

cur.execute("SELECT * FROM test.ani")
for r in cur:
    print(r)
    #print("name:" + str(r[0]) + "  color:" + str(r[2]) + " age:" + str(r[1]))

cur.execute("DROP TABLE IF EXISTS t_table")

sql = """CREATE TABLE t_table(
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cur.execute(sql)

sql = """INSERT INTO t_table(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cur.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 如果发生错误则回滚
    conn.rollback()


sql = "DELETE FROM ani WHERE id > '%d'" % (20)
try:
   # 执行SQL语句
   cur.execute(sql)
   # 提交修改
   conn.commit()
except:
   # 发生错误时回滚
   conn.rollback()

cur.close()
conn.close()