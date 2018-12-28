# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28
from  . import auth


@auth.route('/')
def index():
    return 'this is ahth index'