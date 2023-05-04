# built-in packages
import sqlite3
import contextlib

# ---------------------------------------------------------------------------- #
#                                database utils                                #
# ---------------------------------------------------------------------------- #

def Database(path = "db.sqlite3"):
    # 连接数据库（如果文件不存在会自动创建SQLite3数据库文件）
    db = sqlite3.connect(path)
    # 初始化
    # SQL语句在大二下学期数据库课程里会学到的
    db.execute("""
        CREATE TABLE IF NOT EXISTS jobinfo(
            id INTEGER PRIMARY KEY ASC,
            workname TEXT NOT NULL,
            company TEXT NOT NULL,
            salary INTEGER CHECK(salary>=0),
            area TEXT,
            educationalbackground INTEGER
        )""")
    db.execute("CREATE TABLE IF NOT EXISTS account(username TEXT UNIQUE NOT NULL, password TEXT)")
    return contextlib.closing(db)

def Q(s):
    return f"%{s}%"