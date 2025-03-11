# 配置文件

import os

class Config:
    """默认配置"""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"  # 用于会话和表单的加密
    DEBUG = False  # 生产环境应设为 False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///site.db"  # 数据库 URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭数据库修改跟踪，减少性能开销
    SESSION_COOKIE_SECURE = True  # 仅在 HTTPS 下发送 Cookie
    PERMANENT_SESSION_LIFETIME = 3600  # Session 超时时间（秒）

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True  # 开启调试模式
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"  # 使用 SQLite 作为开发数据库

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True  # 启用测试模式
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"  # 测试环境使用独立数据库

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql://user:password@localhost/prod_db"

# 选择环境
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
