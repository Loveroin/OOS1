# Flask初始化文件

#导入flask外部库
from flask import Flask
from config import Config

def app(config_name = 'default'):

    # 创建 Flask 实例
    app = Flask(__name__)

    # 从 config.py 文件中读取配置
    app.config.from_object(Config[config_name])

    # 注册路由
    from .routes import routes
    app.register_blueprint(routes)

    return app
