# -*- coding: utf-8 -*-
#开启蓝图
# @Author  : joker
# @Date    : 2018-12-27

from  flask import  Blueprint

main = Blueprint('main',__name__,template_folder="templates")

from ..main import views, errors
