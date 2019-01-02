/**
 *  注册相关js
 * Created by joker on 2019/1/2.
 */
var exist_phone_state = false;
var exist_image_code_state = false;
function user_mobile_err_content() {
    if (exist_phone_state === false) {
        $("#register-mobile-err").html("请输入您的手机号").show();
    }
}
function user_imageCaptchaValue_tip_content() {
    if (exist_image_code_state === false) {
        $("#user_imageCaptcha_err").html("请输入验证码，不区分大小写").show();
    }
}
/**
 * 检查手机号是否合法
 * @param {type} is_submit
 * @returns {Boolean}
 */
function check_mobile(is_submit) {
    //验证手机号码格式   checkTel
    var register_mobile = gtrim($("#register_mobile").val());
    if (register_mobile.length <= 0) {
        $("#register-mobile-err").show();
        if (is_submit === false) {
            $("#register-mobile-err").html("请输入您的手机号");
            return false;
        } else {
            $("#register-mobile-err").html("");
            return true;
        }

    } else if (checkTel(register_mobile) === false) {
        $("#register-mobile-err").show();
        $("#register-mobile-err").html("手机格式不正确");
        return false;
    } else if (is_submit === false) {
        var params = "identity=" + encodeURIComponent(register_mobile);
        handledata('post', jsroot + "/auth/check_mobile", params, 'json', showMessage);
        return true;
    }

}
/**
 * 效验图片验证码
 */
function check_image_captcha(is_submit) {
    var cellImageCaptcha = gtrim($("#imageCaptchaValue").val());
    if (cellImageCaptcha.length <= 0) {
        $("#user_imageCaptcha_err").show();
        if (is_submit ===false) {
            $("#user_imageCaptcha_err").html("请输入验证码，不区分大小写");
            return false;
        } else {
            $("#user_imageCaptcha_err").html("");
            return true;
        }
    } else if (is_submit == false) {
        var params = "image_captcha=" + encodeURIComponent(cellImageCaptcha)+"&image_code_id="+encodeURIComponent(imageCodeId);
        handledata('post', jsroot+"/auth/check_image_captcha", params, 'json', callResults);
        return true;
    }
}
//验证手机回调函数
function showMessage(msg_back) {
    if (msg_back.status == "0") {
        $("#register-mobile-err").show();
        $("#register-mobile-err").html("");
        exist_phone_state = true;
    } else {
        $("#register-mobile-err").show();
        $("#register-mobile-err").html(msg_back.errmsg);
        exist_phone_state = false;
    }
}
function callResults(msg_back) {
    if(msg_back.status == "0"){
         $("#user_imageCaptcha_err").show();
         $("#user_imageCaptcha_err").html("");
         exist_image_code_state = true;
    }else{
        $("#user_imageCaptcha_err").show();
        $("#user_imageCaptcha_err").html(msg_back.errmsg);
    }
}
$(function () {
    $('.shutoff').click(function () {
        $(this).closest('form').hide();
    })
    // TODO 注册按钮点击
    $(".register_form_con").submit(function (e) {
        // 阻止默认提交操作,不让其往默认的action提交
        e.preventDefault()

        // 取到用户输入的内容
        var mobile = $("#register_mobile").val()
        var smscode = $("#smscode").val()
        var password = $("#register_password").val()

        if (!mobile) {
            $("#register-mobile-err").show();
            return;
        }
        if (!smscode) {
            $("#register-sms-code-err").show();
            return;
        }
        if (!password) {
            $("#register-password-err").html("请填写密码!");
            $("#register-password-err").show();
            return;
        }

        if (password.length < 6) {
            $("#register-password-err").html("密码长度不能少于6位");
            $("#register-password-err").show();
            return;
        }

        // 发起注册请求
        //拼接请求参数
        var params = {
            "mobile": mobile,
            "sms_code": smscode,
            "password": password
        }
        /*
         $.ajax({
         url:'/passport/register',
         type:'post',
         data:JSON.stringify(params),
         contentType:'application/json',
         headers:{'X-CSRFToken':getCookie('csrf_token')},
         success: function (resp) {
         //判断是否注册成功
         if(resp.errno == '0'){
         //重新加载当前页面
         window.location.reload()
         }else{
         alert(resp.errmsg);
         }
         }
         })
         */
    })
    // //点击输入框，提示文字上移
    // $('.form_group').on('click focusin', function () {
    //
    // })
    generateImageCode()
})
