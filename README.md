# flasky

 结构说明：

	flasky/
	├── README.md
	├── app
	│   ├── __init__.py
	│   ├── api
	│   │   └── v1
	│   │       ├── __init__.py
	│   │       └── views.py
	│   ├── auth
	│   │   ├── __init__.py
	│   │   ├── forms.py
	│   │   └── views.py
	│   ├── common
	│   │   ├── common.py
	│   │   ├── constants.py
	│   │   └── response_code.py
	│   ├── log.py
	│   ├── main
	│   │   ├── __init__.py
	│   │   ├── errors.py
	│   │   └── views.py
	│   ├── models.py
	│   ├── static
	│   │   ├── css
	│   │   ├── images
	│   │   ├── js
	│   ├── templates
	│   │   ├── 404.html
	│   │   ├── 500.html
	│   │   ├── auth
	│   │   │   ├── login_view.html
	│   │   │   ├── register_view.html
	│   │   │   └── unconfirmed.html
	│   │   ├── layouts
	│   │   │   └── layout.html
	│   │   └── site
	│   │       └── index.html
	│   └── vendors
	│       ├── __init__.py
	│       └── captcha
	│           ├── __init__.py
	│           ├── captcha.py
	│           └── fonts
	├── config.py
	├── logs
	├── manage.py
	├── requirements
	│   └── common.txt
	└── tests
	    └── __init__.py
 项目启动步骤

    使用数据迁移命令创建数据库

    python manage.py db init 初始化数据库

    python manage.py db migrate 提交修改

    python manage.py db upgrade 执行修改

 启动项目服务

     python manage.py runserver -d

    浏览器访问：http://127.0.0.1:5000/


    浏览器输出：

        This Is Project Index

    项目搭建成功

 用户获取方法：

    is_authenticated：属性，True如果用户具有有效凭据或False其他。

    is_active：True如果用户的帐户处于活动状态或False其他情况下的属性。

    is_anonymous：False适用于普通用户和True特殊匿名用户的属性。

    get_id()：一种方法，以字符串形式返回用户的唯一标识符

用户权限效验：

    @login_required  效验用户必须登录在可以访问，使用方法只需将此装饰器放置要修饰的方法即可


判断用户是否登录：

Example Code:

    {% if current_user.is_authenticated %}
            current_user.属性值，即可调用出用户信息
    {% endif %}


数据库更新命令：

Example:

python3 manage.py db history   //查看版本号

python 文件 db migrate -m"新版本名(注释)"

python 文件 db downgrade(upgrade) 版本号
