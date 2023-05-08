## 如何运行
### 环境配置
首先将仓库拉取到本地：
```bash
$ git clone https://github.com/sumsc-caa/pandora-2023-A-demo.git
$ cd pandora-2023-A-demo
```
然后使用python-venv创建并激活虚拟环境（参见[官方文档](https://docs.python.org/zh-cn/3/library/venv.html)）
```bash
$ python -m venv ./venv
> .\env\Scripts\activate     # for Windows
$ source ./venv/bin/activate # for Linux
```

安装依赖：
```bash
(venv)$ pip install -r requirements.txt
```

### 运行示例
以正常模式启动：
```bash
(venv)$ flask run
```
以调试（debug）模式启动
```bash
(venv)$ flask run --debug
```

启动后使用浏览器访问 http://127.0.0.1:5000 即可（这是默认地址，请查看上条指令的命令行输出以获得实际的地址）。

### 其它信息
测试账号：
- 用户名：test
- 密码：test

## 项目结构
```raw
pandora-2023-A-demo
├── app.py            # 主程序
├── database.py       # 数据库相关函数
├── db.sqlite3        # SQLite文件（数据库文件）
├── README.md         # 这个文档
├── requirements.txt  # 项目依赖
├── static            # 静态文件
│   ├── css           # CSS文件
│   │   ├── bootstrap.min.css
│   │   └── index.css
│   └── js            # Javascript文件
│       └── bootstrap.min.js
└── templates         # html模板
    ├── index.html    # 主页的模板
    ├── jump.html     # 跳转页的模板
    ├── login.html    # 登录页的模板
    └── register.html # 注册页的模板
```
 
### 相关资源
- flask库官方文档：https://flask.palletsprojects.com/
- jinja2库中文文档：https://docs.jinkan.org/docs/jinja2/
- sqlite3库官方中文文档：https://docs.python.org/zh-cn/3/library/sqlite3.html
- SQLite官网：https://www.sqlite.org/index.html
- HTML参考：https://developer.mozilla.org/zh-CN/docs/Web/HTML
- CSS参考：https://developer.mozilla.org/zh-CN/docs/Web/CSS
- Bootstrap官方文档：https://getbootstrap.com/docs/5.2/getting-started/introduction/



