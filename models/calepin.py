# -*- coding: utf-8 -*-
db = DAL("sqlite://storage.sqlite")

db.define_table('blog_post_category',
                Field('id', unique=True),
                Field('title', unique=True),
                Field('description'),
                format = '%(title)s')

db.define_table('blog_post',
                Field('id', unique=True),
                Field('category', 'reference blog_post_category'),
                Field('title'),
                Field('intro'),
                Field('text'),
                format = '%(title)s')

db.blog_post_category.requires = IS_NOT_IN_DB(db, db.blog_post_category.title)
db.blog_post.category.requires = IS_IN_DB(db, db.blog_post_category, '%(title)s')
db.blog_post_category.title.requires = IS_NOT_EMPTY()
db.blog_post.title.requires = IS_NOT_EMPTY()
