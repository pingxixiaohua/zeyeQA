from flask import Flask
import config
from exts import db, mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 关联config文件
app.config.from_object(config)
# 绑定orm对象数据库
db.init_app(app)
# 绑定邮箱
mail.init_app(app)

migrate = Migrate(app,db)

# 注册蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

# blueprint
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
