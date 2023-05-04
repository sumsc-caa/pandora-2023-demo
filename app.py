# built-in packages
from hashlib import pbkdf2_hmac

# third-party packages
from flask import Flask
from flask import render_template
from flask import request, session

# local files
from database import Database, Q


# ---------------------------------------------------------------------------- #
#                                    server                                    #
# ---------------------------------------------------------------------------- #

app = Flask(__name__)

# 用于加密的key，正常情况下不应该公开，但是这里是演示项目，所以就无所谓咯
app.secret_key = bytes.fromhex('5a1e389584524b30f0f47299db0d88cdbb411006b21e946f6149d170f734ff18')
password_salt = bytes.fromhex('9069949f8a6725e46c2e2a63509bb2777cac80494ecba2c191f088ca04870ab7')
password_iters = 10000 # 哈希函数的迭代次数

# ------------------------------- server utils ------------------------------- #
def password_hash(pwd: str):
    # 密码不能用明文存储哦
    return pbkdf2_hmac('sha256', pwd.encode(), password_salt, password_iters).hex()

# --------------------------------- templates -------------------------------- #
template_consts = {
    "edulist": ['', '博士研究生', '硕士研究生', '大学本科', '大学专科', '中等专科', '职业高中', '技工学校', '普通高中', '初中', '小学', '其他'],
}

@app.context_processor
def inject_consts():
    """注入渲染模板时使用的常量"""
    return template_consts

def jump(message, dest = '/', action = '返回主页', countdown=5):
    """显示跳转页"""
    return render_template("jump.html", message=message, destination=dest, action=action, count=countdown)

# --------------------------------- handlers --------------------------------- #
@app.route("/")
@app.route("/index.html")
@app.route("/search", methods = ["GET"])
def index():
    """处理查询请求（主页对应空查询）"""
    # 从session中获取用户名，如果未登录则为None
    username = session.get("username", None)

    # 获取请求参数
    workName = request.args.get("workName", "")
    companyName = request.args.get("companyName", "")
    salary = request.args.get("salary", 0, type=int)
    area = request.args.get("area", "")
    educationalBackground = request.args.get("educationalBackground", 0, type=int)
    
    with Database() as db:
        # 访问数据库，执行查询语句
        cursor = db.execute("""
            SELECT * FROM jobinfo WHERE 
                workname LIKE ? 
                AND company LIKE ?
                AND salary >= ? 
                AND area LIKE ?
                AND (? = 0 OR educationalbackground = ?)""",
            (Q(workName), Q(companyName), salary, Q(area), educationalBackground, educationalBackground))
        results = cursor.fetchall()
    # print(results)
    
    return render_template("index.html", query = request.args, username = username, jobs = results)

@app.route("/login", methods = ["GET", "POST"])
def login():
    """登录"""
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if not username or not password:
        errmsg = "请输入用户名与密码"
    else:
        with Database() as db:
            cursor = db.execute("SELECT * FROM account WHERE username = ?", (username, ))
            result = cursor.fetchone()
        if result is None:
            errmsg = "该用户不存在"
        else:
            _, correct_password = result
            password = password_hash(password)
            if correct_password == password:
                # 设置session
                session['username'] = username
                return jump("登录成功", '/', '返回主页')
            else:
                errmsg = "密码错误"

    return render_template("login.html", username = username, errmsg = errmsg)

@app.route("/logout")
def logout():
    """登出"""
    if "username" in session:
        del session['username']
    return jump("已成功登出")
    
@app.route("/register", methods = ["GET", "POST"])
def register():
    """注册"""
    if request.method == "GET":
        return render_template("register.html")
    
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if not username or not password:
        errmsg = "请输入用户名与密码"
    else:
        with Database() as db:
            cursor = db.execute("SELECT * FROM account WHERE username = ?", (username, ))
            result = cursor.fetchone()
            if result is not None:
                errmsg = "用户名已存在"
            else:
                cursor = db.execute("INSERT INTO account VALUES (? , ?)", (username, password_hash(password)))
                db.commit()
                return jump("注册成功", '/login', '跳转至登录页')

    return render_template("register.html", errmsg = errmsg)
