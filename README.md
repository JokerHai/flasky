# flasky

 结构说明：

     flasky/
    ├── app //程序包
    │   ├── api //接口包
    │   │   └── __init__.py
    │   ├── auth
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── errors.py
    │   │   ├── __init__.py
    │   │   └── views.py
    │   └── models.py
    ├── config.py
    ├── manage.py
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

     python3 manage.py runserver -d

    浏览器访问：http://127.0.0.1:5000/


    浏览器输出：

        this is project index

    项目搭建成功


