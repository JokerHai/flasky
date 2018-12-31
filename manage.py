# -*- coding: utf-8 -*-
# 项目启动文件
# @Author  : joker
# @Date    : 2018-12-27
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import create_app, db
from app.models import User,News,Comment,CommentLike,Category

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db,
                User=User,News=News,
                Comment=Comment,CommentLike=CommentLike,
                Category=Category
                )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

