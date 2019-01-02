# -*- coding: utf-8 -*-
# 公共方法
# @Author  : joker
# @Date    : 2019-01-02
import re

# 效验手机号
def check_mobile(mobile):
    return mobile if re.match("1[3-9]\d{9}", mobile) else False


