# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28
from  . import auth


@auth.route('/')
def index():
    return 'This Is Auth Index'