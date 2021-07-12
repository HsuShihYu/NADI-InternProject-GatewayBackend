from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
# MySQL configurations


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '880117qazwsX/'
app.config['MYSQL_DATABASE_DB'] = 'Test'
app.config['MYSQL_DATABASE_HOST'] = '172.18.0.1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹

mysql.init_app(app)
