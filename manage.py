# -*- coding: utf-8 -*-
# 项目启动文件
# @Author  : joker
# @Date    : 2018-12-27

import os

from app import create_app, db

from app.models import Author, Book

from flask_script import Manager, Shell

from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Author=Author, Book=Book)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
