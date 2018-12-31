# -*- coding: utf-8 -*-
#首页入口文件
# @Author  : joker
# @Date    : 2018-12-27
from  flask import render_template
from ..main import main

@main.route('/',methods = ['GET'])
def index():
    return  render_template("site/index.html")
