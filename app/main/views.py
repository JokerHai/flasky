# -*- coding: utf-8 -*-
#首页入口文件
# @Author  : joker
# @Date    : 2018-12-27

from ..main import main

@main.route('/',methods = ['GET'])
def index():

    return 'this is project index'

@main.route('/user')
def user():
    return 'this is user Controller'