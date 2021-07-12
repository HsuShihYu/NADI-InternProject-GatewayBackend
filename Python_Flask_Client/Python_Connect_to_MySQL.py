#Connect to MySQL
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","880117qazwsX/","Test")


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 建置 Database (建置時pymysql.connect 後面不用加 database 名稱)
# cursor.execute("CREATE DATABASE gateway_db")

# 建置 system_spec_table 
cursor.execute("CREATE TABLE OPCDA_Configuration(DA_INDEX INT AUTO_INCREMENT PRIMARY KEY, \
  DA_SERVER_NAME VARCHAR(255), DA_SERVER_IP VARCHAR(255), DA_TIMEOUT INT, DA_RECORD_BAD INT, DA_RECORD_ERROR INT,\
     LOG_FILE_MAX_COUNT INT, SYSTEM_ID VARCHAR(255), TAG_NAMES_CSV VARCHAR(255), \
      API_POST_URL VARCHAR(255), API_POST_TIMEOUT INT, API_SEND_BAD INT, API_SEND_ERROR INT, REFRESH_RATE INT)")

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x) 
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()

# #insert data
# #!/usr/bin/python3
 
# import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","880117qazwsX/","Test")
 
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 插入语句
# for i in range(49):
#     i = i + 2
#     sql = "INSERT INTO system_spec_table(system_id, system_name, time_stamp, time_zone, object_id, value, object_time_stamp) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
#     val = (i, "TEST", 1234567890, "ASIA/TAIPEI", "BL_202_Status_0000099", 14789, 1583816587)
#     try:
#         # 执行sql语句
#         cursor.execute(sql, val)
#         print(i)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 如果发生错误则回滚
#         db.rollback()
#         print('fail')
 
# #关闭数据库连接
# db.close()



# #find data
# #!/usr/bin/python3
 
# import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","880117qazwsX/","my_db" )
 
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()
 
# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#        # 打印结果
#       print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")
 
# # 关闭数据库连接
# db.close()

# #update data
# #!/usr/bin/python3
 
# import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","880117qazwsX/","my_db")
 
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()
 
# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
 
# # 关闭数据库连接
# db.close()

# #delete data
# #!/usr/bin/python3
 
# import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","880117qazwsX/","my_db" )
 
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()
 
# # SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (21)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
 
# # 关闭连接
# db.close()