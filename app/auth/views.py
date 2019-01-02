# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28
import random

from flask import current_app, render_template, request, make_response, jsonify
from app import redis_store
from app.common import constants
from app.common.common import check_mobile
from app.common.response_code import RET
from app.vendors.captcha.captcha import captcha
from ..models import User
from . import auth


# 弹出注册页面
@auth.route('/register_view', methods=['GET'])
def register_view():
    return render_template("auth/register_view.html")


# 检查手机号是否合法
@auth.route('/check_mobile', methods=['POST'])
def check_mobile():
    try:
        # 获取参数
        identity = request.form.get("identity")
        if not identity:
            return jsonify(status=RET.PARAMERR, errmsg="手机号为空")
        # 效验用户是否已经注册
        user = User.query.filter_by(mobile=identity).first()
        if user is not None:
            return jsonify(status=RET.RET.DATAEXIST, errmsg="您已注册，可进行登录操作")

        return jsonify(status=RET.OK, errmsg="成功")
    except Exception as e:
        current_app.logger.error(e)
    return jsonify(status=RET.DBERR, errmsg="数据异常，请联系管理员")

@auth.route('/check_image_captcha',methods = ['POST'])
def check_image_captcha():
    try:
        image_captcha = request.form.get("image_captcha")
        image_code_id = request.form.get("image_code_id")
        if not  image_captcha:
            return jsonify(status = RET.PARAMERR,errmsg = "请输入验证码")
        flag = redis_store.get("image_code:%s"%image_code_id+image_captcha.lower())
        if flag:
            return jsonify(status = RET.OK, errmsg = "成功")
        else:
            return jsonify (status = RET.DATAERR, errmsg = "验证码错误，请重新输入")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=RET.SERVERERR, errmsg="数据异常，请联系管理员")
# 获取图片验证码
@auth.route('/captcha_image')
def captcha_image():
    # 获取参数
    cur_id = request.args.get("cur_id")
    pre_id = request.args.get("pre_id")

    # 调用generate_captcha获取图片验证码编号,验证码值,图片(二进制)
    name, text, image_data = captcha.generate_captcha()

    # 3.将图片保存至redis
    try:
        # 参数1: key,  参数2: value,  参数3: 有效期
        redis_store.set("image_code:%s" % cur_id+text.lower(), text.lower(), constants.IMAGE_CODE_REDIS_EXPIRES)
        # 4.判断是否有上一次的图片验证码
        if pre_id:
            redis_store.delete("image_code:%s" % pre_id)
    except Exception as e:
        current_app.logger.error(e)
        return "图片验证码操作失败"
    # 5返回图片
    response = make_response(image_data)
    response.headers["Content-Type"] = "image/png"
    return response


@auth.route('/sms_code', methods=['GET'])
def sms_code():
    try:
        dist_data = request.json

        if dist_data is None:
            return jsonify(status=RET.REQERR, errmsg="非法请求或请求次数受限")

        mobile = dist_data.get("mobile")
        img_code = dist_data.get("image_code")
        img_code_id = dist_data.get("image_code_id")

        if not mobile:
            return jsonify(status=RET.PARAMERR, errmsg="手机号为空")

        if not img_code:
            return jsonify(status=RET.PARAMERR, errmsg="图片验证码为空")

        if not img_code_id:
            return jsonify(status=RET.PARAMERR, errmsg="图片ID为空")

        if not check_mobile(mobile):
            return jsonify(status=RET.DATAERR, errmsg="手机号的格式错误")

        redis_img_code = redis_store.get("img_code:%s" % img_code)

        if redis_img_code is None:
            return jsonify(status=RET.DBERR, errmsg="数据错误，请联系管理员")

        if img_code.upper() != redis_img_code.upper():
            return jsonify(status=RET.DATAERR, errmsg="图片验证码填写错误")

        flag = redis_store.delete("img_code:%s" % img_code)
        if not flag:
            return jsonify(status=RET.DBERR, errmsg="操作数据库失败")
        # 生成一个随机短信验证码，判断验证码是否发送成功
        verity_code = "%06d" % random.randint(0, 999999)
        if not verity_code:
            redis_flag = redis_store.set("sms_code:%s" % mobile, verity_code, constants.SMS_CODE_REDIS_EXPIRES)

            if redis_flag is False:
                return jsonify(status=RET.DBERR, errmsg="图片验证码保存到redis失败")
        # 10. 返回响应
        return jsonify(status=RET.OK, errmsg="短信发送成功")
    except Exception as e:

        current_app.logger.error(e)

        return jsonify(status=RET.DBERR, errmsg="删除redis图片验证码失败")
