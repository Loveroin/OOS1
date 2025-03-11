# 路由函数，所有路由全部在此处列出

from flask import Blueprint, render_template, url_for

# 创建蓝图
main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

