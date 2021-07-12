#insert data
#!/usr/bin/env python
#coding=utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","880117qazwsX/","Test")
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()