# flasky

 结构说明：

    flasky/  //程序包
    ├── app
    │   ├── api  //api包
    │   │   └── v1
    │   │       ├── __init__.py
    │   │       └── views.py
    │   ├── auth    //认证 授权
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── __init__.py
    │   ├── log.py
    │   ├── main  //py程序包
    │   │   ├── errors.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   ├── models.py   //数据库模型
    │   ├── static
    │   │   └── ting.jpeg
    │   └── templates
    │       └── index.html
    ├── config.py //全局配置文件
    ├── logs      //日志
    ├── manage.py  //启动文件
    ├── README.md
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