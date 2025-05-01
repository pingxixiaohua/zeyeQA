from flask import Blueprint, render_template, jsonify
from exts import mail,db
from flask_mail import Message
from flask import request
import random
import string
from models import EmailCaptchaModel
from .forms import RegisterForm

# /auth开头
bp = Blueprint("auth", __name__, url_prefix="/auth")

# /auth/login
@bp.route('/login')
def login():
    pass

@bp.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        # 表单验证：flask-wtf
        form = RegisterForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return "fail"  

@bp.route('/cpatcha/email')
def get_email_cpatcha():
    email = request.args.get("email")
    # 随机数验证码
    source = string.digits*4
    captcha = random.sample(source,4)
    captcha = "".join(captcha)
    message = Message(subject="者也问答验证码", recipients=[email], body=f"您的验证码是：{captcha}，<br />请不要告诉他人")
    mail.send(message)
    # 将验证码信息存储
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code": 200, "message":"", "data": None})

@bp.route('/mail_test')
def mail_test():
    message = Message(subject="邮箱测试", recipients=["1608386461@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    # msg = EmailMessage(
    #     subject="Flask-Mailman 测试邮件",
    #     body="这是一封通过 Flask-Mailman 发送的测试邮件。",
    #     from_email="3189167918@qq.com",
    #     to=["473674495@qq.com"]
    # )
    # mail.send_messages(msg)
    return "邮件发送成功"