# -*- coding:utf-8 -*-

def beautiful_context(app, pagename, templatename, context, doctree):
    '''
    修改context中的body属性，来处理 **和中文** 相关的两个问题：

        - 由于换行符"\n"而导致的空格
        - 由于 inline marker 而导致的空格
    '''
    pass

def setup(app):
    app.connect('html-page-context', beautiful_context)
