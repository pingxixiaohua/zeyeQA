SECRET_KEY = "SAFHIEOAWFJLAFWEIFHEA"

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zeyeoa'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI= f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI

MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '3189167918@qq.com'
MAIL_PASSWORD = 'ccxnmegdynqudcef'
MAIL_DEFAULT_SENDER = '3189167918@qq.com'

# config.py
# MAIL_SERVER = 'smtp.qq.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True  # 与 MAIL_PORT 465 配合使用
# MAIL_USERNAME = '3189167918@qq.com'
# MAIL_PASSWORD = 'ccxnmegdynqudcef'
# MAIL_DEFAULT_SENDER = '3189167918@qq.com'

# ccxnmegdynqudcef