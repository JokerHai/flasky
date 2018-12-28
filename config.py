# -*- coding: utf-8 -*-
# 项目配置文件
# @Author  : joker
# @Date    : 2018-12-27


class Config:
    # 密钥
    SECRET_KEY = "QWE123!@#"

    # 该字段增加了大量的开销,会被禁用,建议设置为False
    SQLALCHEMY_TRACK_MODIFICATIONS = False





    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@172.16.150.128:3306/my_db"



config = {
    'development' : DevelopmentConfig,

    'default'     : DevelopmentConfig
}
