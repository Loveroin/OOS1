# Flask初始化文件

#导入flask外部库
from flask import Flask
from config import config

def app(config_name = 'default'):

    # 创建 Flask 实例
    app = Flask(__name__)

    # 从 config.py 文件中读取配置
    app.config.from_object(config[config_name])

    # 注册路由
    from .routes import main
    app.register_blueprint(main)

    return app
