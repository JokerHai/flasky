# -*- coding: utf-8 -*-
#创建APP 应用工程模式
# @Author  : joker
# @Date    : 2018-12-27
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config



db = SQLAlchemy()

def create_app(config_name):

    app = Flask (__name__)

    #加载配置文件
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)


    #注册蓝图

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    from .api.v1 import api as api_blueprint

    app.register_blueprint(api_blueprint,url_prefix ='/api')

    db.init_app(app)

    return  app

