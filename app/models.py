# -*- coding: utf-8 -*-
#数据模型
# @Author  : joker
# @Date    : 2018-12-27
from . import db

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))

    #关系属性
    books = db.relationship("Book",backref="author")

#书籍模型(多方)
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))

    #外键
    author_id = db.Column(db.Integer,db.ForeignKey(Author.id))

