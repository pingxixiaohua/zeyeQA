from flask import Flask, session, g
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
# 模块化

# flask db init: 只执行一次
# flask db migrate: 将orm模型生成迁移脚本
# flask db upgrade: 将迁移脚本映射到数据库中

# before_request/ bdefore_first_request/ ofter_reguest
# hook
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

@app.context_processor
def my_context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    app.run()
