# 苏州大学计算机爱好者协会 2023魔盒挑战 demo项目
本项目是一个及其简易的招聘信息发布与搜索平台，仅有信息展示、信息检索、账户系统三个功能。

需要说明的是，考虑到参赛者大多没有接触过Web开发，目前工业界Web开发中更为流行的前后端分离、响应式网站设计等理念与技术在本项目中均没有采用，因为这些技术对前端的开发能力有较高的要求，包括对JavaScript、React/Vue等的掌握，这对于没接触过前端的同学有较高的学习门槛，较难在短时间内达到能自由编写代码的水平。
本项目（以及比赛项目）作为部分同学的Web入门项目，为了降低门槛（同时让更多人能参与进来），采取了较为简单（与原始）的方式，即由基于flask的后端程序（即本院大部分同学都学习过的Python）渲染页面、处理表单逻辑，这样前端部分只需要HTML与一些CSS的知识。
虽然这比较原始，但是个人认为这种模式的项目作为部分同学Web开发的入门项目也是不错的（随着技术的发展历程由浅入深）。
在比赛结束后有意向接着学习Web开发的同学可以参考 https://github.com/liyupi/code-roadmap/tree/main/docs/roadmap 。

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

### 如何向

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



