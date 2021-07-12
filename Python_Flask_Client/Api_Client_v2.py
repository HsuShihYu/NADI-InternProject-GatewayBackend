import requests
import json
import pymysql

# 讀檔案到 input list
f = open(r'input.txt')
r = f.read()
input = r.split(' ')
print(input)

url = input[0]
index = 0
# Send data to Backend Api
#!/usr/bin/python3
while True:
    #!/usr/bin/python3
    # 打開數據庫
    db = pymysql.connect("localhost",input[1], input[2], input[3])
    # 使用cursor()方法獲取操作指標
    cursor = db.cursor()
    # SQL 查詢
    sql = "SELECT * FROM " + str(input[4]) + " WHERE system_id >= '" + str(index) + "'"
    data = {}
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    if len(results) == 0:
        print("目前資料庫內資料皆已上傳\n")
        break
    else:
        print("繼續上傳新資料到 Backend Api \n")
        while(len(results) != 0):
            try:
                data.setdefault("System",results[0][1])
                data.setdefault("TimeStamp",results[0][2])
                data.setdefault("TimeZone",results[0][3])
                Data = []
                for row in results:
                    index = index + 1
                    obj_data = {}
                    obj_data.setdefault("ObjectId",row[4])
                    obj_data.setdefault("Value",row[5])
                    obj_data.setdefault("TimeStamp",row[6])
                    Data.append(obj_data)
                    headers = {'Content-Type':'application/json'}
                    r = requests.post(url, headers=headers, data=json.dumps(data))
                    #print(r.status_code)
                    #print(r.text)
                    print("row number = " + str(row[0]) + " index = " + str(index))
                break
            except:
                print("Error: unable to fetch data")
                break
    #關閉資料庫
    db.close()




