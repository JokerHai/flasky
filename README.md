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


