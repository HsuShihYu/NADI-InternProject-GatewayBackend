import pymysql
import os
import json
import time
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request, render_template, send_from_directory
from flask import send_file
from configparser import ConfigParser



#create opcda
@app.route('/test/v1/create_opcda', methods=['POST'])
def create_opcda():
    try:
        sqlQuery = "SELECT * FROM System_Realtime_Data ORDER BY system_id DESC LIMIT 1"
        con_default = mysql.connect()
        cursor = con_default.cursor()
        cursor.execute(sqlQuery)
        result = cursor.fetchall()
        if len(result) == 0:
            index = 0
        else:
            index = result[0][0]
        cursor.close()
        con_default.close()
        
        _json = request.json
        _system_name = _json["System"]
        _time_stamp = _json["timeStamp"]
        _time_zone = _json["TimeZone"]
        _data = _json["values"]
        for row in _data:
            index = index + 1
            _system_id = index
            _object_id = row["id"]
            _value = row["v"]
            _object_time_stamp = row["t"]

            # insert record in database
            sqlQuery = "INSERT INTO System_Realtime_Data(system_id, system_name, time_stamp, time_zone, object_id, value, object_time_stamp) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            data = (_system_id, _system_name, _time_stamp, _time_zone, _object_id, _value, _object_time_stamp)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, data)
            conn.commit()

            cursor.close()
            conn.close()
        res = jsonify("Create successfully.")
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
        res2 = jsonify("Fail")
        res2.status_code = 400
        return res2
 

# create account
@app.route('/test/v1/account_create', methods=['POST'])
def create_account():
    try:
        # connect to mySQL
        conn = mysql.connect()
        cursor = conn.cursor()

        _json = request.json
        _db_username = _json["DB_User"]
        _db_password = _json["DB_Password"]
        _db_ip = _json["DB_IP"]
        _db_port = _json["DB_Port"]
        _backend_api_url = _json["Backend_Api_Url"]
        _refresh_number = _json["Refresh_Number"]

        sqlQuery = "INSERT INTO System_Configuration(DB_User, DB_Password, DB_IP, DB_Port, Backend_Api_Url, Refresh_Number)\
             VALUES(%s, %s, %s, %s, %s, %s)"
        data = (_db_username, _db_password, _db_ip, _db_port, _backend_api_url, _refresh_number)
        cursor.execute(sqlQuery, data)
        conn.commit()
        cursor.close()
        conn.close()

        res = jsonify("User:root create successfully!")
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
        res2 = jsonify("Fail")
        res2.status_code = 400
        return res2

# create account
@app.route('/test/v1/account_get_default', methods=['GET'])
def get_default_account():
    data = {
     "DB_User": "root",
     "DB_Password": "880117qazwsX/", 
     "Refresh_Number": 100000,
     "DB_IP": "172.18.0.1",
     "DB_Port": "5000",
     "Backend_Api_Url": "http://192.168.1.133:9000/ocms/api/insertSensorData"
    }
    _data = jsonify(data)
    return _data

# create OPCDA_Config
@app.route('/test/v1/opcda_config_create', methods=['POST'])
def create_opcda_config():
    try:
        # connect to mySQL
        conn = mysql.connect()
        cursor = conn.cursor()

        _json = request.json
        _DA_SERVER_NAME = _json["DA_SERVER_NAME"]
        _DA_SERVER_IP = _json["DA_SERVER_IP"]
        _DA_TIMEOUT = _json["DA_TIMEOUT"]
        _DA_RECORD_BAD = _json["DA_RECORD_BAD"]
        _DA_RECORD_ERROR = _json["DA_RECORD_ERROR"]
        _LOG_FILE_MAX_COUNT = _json["LOG_FILE_MAX_COUNT"]
        _SYSTEM_ID = _json["SYSTEM_ID"]
        _TAG_NAMES_CSV = _json["TAG_NAMES_CSV"]
        _API_POST_URL = _json["API_POST_URL"]
        _API_POST_TIMEOUT = _json["API_POST_TIMEOUT"]
        _API_SEND_BAD = _json["API_SEND_BAD"]
        _API_SEND_ERROR = _json["API_SEND_ERROR"]
        _REFRESH_RATE = _json["REFRESH_RATE"]
        print(_DA_SERVER_NAME)

        sqlQuery = "INSERT INTO OPCDA_Configuration(DA_SERVER_NAME, DA_SERVER_IP, DA_TIMEOUT, DA_RECORD_BAD, DA_RECORD_ERROR, LOG_FILE_MAX_COUNT, SYSTEM_ID, TAG_NAMES_CSV, API_POST_URL, API_POST_TIMEOUT, API_SEND_BAD, API_SEND_ERROR, REFRESH_RATE)\
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (_DA_SERVER_NAME, _DA_SERVER_IP, _DA_TIMEOUT, _DA_RECORD_BAD, _DA_RECORD_ERROR, _LOG_FILE_MAX_COUNT, _SYSTEM_ID, _TAG_NAMES_CSV, _API_POST_URL, _API_POST_TIMEOUT, _API_SEND_BAD, _API_SEND_ERROR, _REFRESH_RATE)
        cursor.execute(sqlQuery, data)
        conn.commit()
        cursor.close()
        conn.close()

        res = jsonify("OPCDA Configuration Create Successfully!")
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
        res2 = jsonify("Fail")
        res2.status_code = 400
        return res2

# create OPCDA_Config
@app.route('/test/v1/get_opcda_config', methods=['GET'])
def get_opcda_config():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM OPCDA_Configuration ORDER BY DA_INDEX DESC LIMIT 1"
        cursor.execute(sqlQuery)
        
        result = cursor.fetchall()
        data = {}
        data.setdefault("DA_INDEX",result[0][0])
        data.setdefault("DA_SERVER_NAME",result[0][1])
        data.setdefault("DA_SERVER_IP",result[0][2])
        data.setdefault("DA_TIMEOUT",result[0][3])
        data.setdefault("DA_RECORD_BAD",result[0][4])
        data.setdefault("DA_RECORD_ERROR",result[0][5])
        data.setdefault("LOG_FILE_MAX_COUNT",result[0][6])
        data.setdefault("SYSTEM_ID",result[0][7])
        data.setdefault("TAG_NAMES_CSV",result[0][8])
        data.setdefault("API_POST_URL",result[0][9])
        data.setdefault("API_POST_TIMEOUT",result[0][10])
        data.setdefault("API_SEND_BAD",result[0][11])
        data.setdefault("API_SEND_ERROR",result[0][12])
        data.setdefault("REFRESH_RATE",result[0][13])

        res = json.dumps(data)
        return res
    
    except Exception as e:
        print(e)
        res2 = jsonify("Fail")
        res2.status_code = 400
        return res2

# create OPCDA_Config
@app.route('/test/v1/get_opcda_config_v2', methods=['GET'])
def get_opcda_config_v2():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM OPCDA_Configuration ORDER BY DA_INDEX DESC LIMIT 1"
        cursor.execute(sqlQuery)
        
        result = cursor.fetchall()
        
        cfg = ConfigParser()
        cfg.add_section('client config')
        cfg.set('client config',"DA_INDEX",str(result[0][0]))
        cfg.set('client config',"DA_SERVER_NAME",str(result[0][1]))
        cfg.set('client config',"DA_SERVER_IP",str(result[0][2]))
        cfg.set('client config',"DA_TIMEOUT",str(result[0][3]))
        cfg.set('client config',"DA_RECORD_BAD",str(result[0][4]))
        cfg.set('client config',"DA_RECORD_ERROR",str(result[0][5]))
        cfg.set('client config',"LOG_FILE_MAX_COUNT",str(result[0][6]))
        cfg.set('client config',"SYSTEM_ID",str(result[0][7]))
        cfg.set('client config',"TAG_NAMES_CSV",str(result[0][8]))
        cfg.set('client config',"API_POST_URL",str(result[0][9]))
        cfg.set('client config',"API_POST_TIMEOUT",str(result[0][10]))
        cfg.set('client config',"API_SEND_BAD",str(result[0][11]))
        cfg.set('client config',"API_SEND_ERROR",str(result[0][12]))
        cfg.set('client config',"REFRESH_RATE",str(result[0][13]))
        # 輸出 ini檔案
        with open('/home/yoyoman/Desktop/Nadi_System/Python_Flask_Server/Gateway_API/upload/config.ini', 'w', encoding='utf-8') as file:
            cfg.write(file)
        
        return send_file('/home/yoyoman/Desktop/Nadi_System/Python_Flask_Server/Gateway_API/upload/config.ini',
                     mimetype='text/csv/ini', 
                     attachment_filename = "config.ini",
                     as_attachment=True)
    
    except Exception as e:
        print(e)
        res2 = jsonify("Fail")
        res2.status_code = 400
        return res2


# Let User dowload csv file
@app.route('/downloads/<filename>') # this is a job for GET, not POST
def plot_csv(filename):
    return send_file('/home/yoyoman/Desktop/Nadi_System/Python_Flask_Server/Gateway_API/upload/' + str(filename),
                     mimetype='text/csv/ini', 
                     attachment_filename=str(filename),
                     as_attachment=True)


# Let Uset uploads csv file to <upload >
basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
ALLOWED_EXTENSIONS = set(['csv','ini'])  # 允许上传的文件后缀

# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 具有上傳功能的頁面
@app.route('/test/upload')
def upload_test():
    return render_template('upload.html')

@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])  # 拼接成合法文件夾地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夾不存在就創建
    f=request.files['myfile']  # 從表單的file字段獲取文件，myfile為該表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上傳的檔案格式
        fname=f.filename
        ext = fname.rsplit('.', 1)[1]  # 獲取文件檔案格式
        unix_time = int(time.time())
        new_filename = str(unix_time)+'.'+ext   # 修改文件名
        f.save(os.path.join(file_dir, new_filename))  #保存文件到upload目錄

        return jsonify({"errno": 0, "errmsg": "上傳成功"})
    else:
        return jsonify({"errno": 1001, "errmsg": "上傳失败"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    