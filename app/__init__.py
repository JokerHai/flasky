# -*- coding: utf-8 -*-
#创建APP 应用工厂模式
# @Author  : joker
# @Date    : 2018-12-27
from flask import Flask

import  redis

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import Session

from config import config

from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

redis_store = None

def create_app(config_name):

    app = Flask (__name__)

    #加载配置文件
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    #CSFR保护APP

    CSRFProtect(app)

    #注册蓝图

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    from .api.v1 import api as api_blueprint

    app.register_blueprint(api_blueprint,url_prefix ='/api')

    db.init_app(app)

    # 配置redis
    global redis_store

    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 设置session保存位置
    Session(app)

    return  app

