import requests
import json
import pymysql

# 讀檔案到 input list
f = open(r'input.txt')
r = f.read()
input = r.split(' ')
print(input)

url = input[0]


# Send data to user && post to Backend Api
#!/usr/bin/python3
# 打開數據庫
db = pymysql.connect("localhost",input[1], input[2], input[3])

# 使用cursor()方法獲取操作指標
cursor = db.cursor()

# SQL 查詢
sql = "SELECT * FROM " + str(input[4]) + " WHERE system_name = '" + str(input[5] + "'")
x = "SELECT * FROM system_spec_table ORDER BY system_id DESC LIMIT 1"
data = {}
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()

while (len(results) != 0):
  try:
    data.setdefault("System",results[0][1])
    data.setdefault("TimeStamp",results[0][2])
    data.setdefault("TimeZone",results[0][3])
    Data = []
    for row in results:
      obj_data = {}
      obj_data.setdefault("ObjectId",row[4])
      obj_data.setdefault("Value",row[5])
      obj_data.setdefault("TimeStamp",row[6])
      Data.append(obj_data)
      headers = {'Content-Type':'application/json'}
      r = requests.post(url, headers=headers, data=json.dumps(data))
      print(r.status_code)
      print(r.text)
    break
  except:
    print ("Error: unable to fetch data")
    break

#关闭数据库连接
db.close()


# 參考 data 傳輸格式

# data = {
#   "System": "Test",
#   "TimeStamp": 1234567890,
#   "TimeZone": "Asia/Taipei",
#   "Data": [
#     {
#       "ObjectId": "BL_202_Run_000001",
#       "Value": "5560",
#       "TimeStamp":1583816575
#     },
#     {
#       "ObjectId": "BL_202_Idle_000007",
#       "Value": "5000",
#       "TimeStamp":1583816580
#     },
#     {
#       "ObjectId": "BL_202_Status_0000055",
#       "Value": "14789",
#       "TimeStamp":1583816587
#     }
#     ]
# }










