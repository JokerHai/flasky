# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28
from flask import current_app,render_template, request,make_response
from app import redis_store
from app.common import constants
from app.vendors.captcha.captcha import captcha
from  . import auth

#弹出注册页面
@auth.route('/register_view',methods = ['GET'])
def register_view():
    return render_template("auth/registerView.html")

#获取图片验证码
@auth.route('/image_code')
def image_code():
    #1.获取参数
    cur_id = request.args.get("cur_id")
    pre_id = request.args.get("pre_id")

    #2.调用generate_captcha获取图片验证码编号,验证码值,图片(二进制)
    name, text, image_data = captcha.generate_captcha()

    #3.将图片保存至redis
    try:
        #参数1: key,  参数2: value,  参数3: 有效期
        redis_store.set("image_code:%s"%cur_id,text,constants.IMAGE_CODE_REDIS_EXPIRES)
        #4.判断是否有上一次的图片验证码
        if pre_id:
            redis_store.delete("image_code:%s"%pre_id)
    except Exception as e:
        current_app.logger.error(e)
        return "图片验证码操作失败"
    #5返回图片
    response = make_response(image_data)
    response.headers["Content-Type"] = "image/png"
    return response