# -*- coding: utf-8 -*-
# 项目配置文件
# @Author  : joker
# @Date    : 2018-12-27


class Config:
    # 密钥
    SECRET_KEY = "QWE123!@#"

    # MYSQL

    # sqlHost地址
    MYSQL_DB_HOST = 'localhost'

    # sql用户名
    MYSQL_DB_USERNAME = 'root'

    # sql密码
    MYSQL_DB_PASSWORD = 'mysql'

    # sql端口
    MYSQL_DB_PORT = "3306"

    # dbName
    MYSQL_DB_NAME = 'my_db'

    # 该字段增加了大量的开销,会被禁用,建议设置为False
    SQLALCHEMY_TRACK_MODIFICATIONS = False





    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True

    type(Config.MYSQL_DB_PORT)

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+\
        Config.MYSQL_DB_USERNAME+":"+Config.MYSQL_DB_PASSWORD+"@"+Config.MYSQL_DB_HOST+":"+Config.MYSQL_DB_PORT+"/"+Config.MYSQL_DB_NAME



config = {
    'development' : DevelopmentConfig,
    'default'     : DevelopmentConfig
}