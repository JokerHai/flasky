# -*- coding: utf-8 -*-
#数据模型
# @Author  : joker
# @Date    : 2018-12-27
from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))


