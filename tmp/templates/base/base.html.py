# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1445478987.826
_enable_loop = True
_template_filename = u'D:\\Projects\\simple_forum\\templates/base/base.html'
_template_uri = u'/base/base.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <meta http-equiv="Content-Type" charset="utf-8" />\r\n    <meta name="viewport" content="width=device-width, initial-scale=1,user-scalable=0" />\r\n    <title></title>\r\n    <!-- <link rel="shortcut icon" type="image/icon" href="/base/static/images/favo.ico" /> -->\r\n    \r\n    <link rel="stylesheet" type=\'text/css\' href="/static/base/css/vendor/bootstrap.min.css" />\r\n    <link rel="stylesheet" type=\'text/css\' href="/static/base/css/flat-ui.min.css" />\r\n    <link rel="stylesheet" type=\'text/css\' href="/static/base/css/base.css" />\r\n    \r\n    <script src="/static/base/js/vendor/jquery.min.js"></script>\r\n    <script src="/static/base/js/flat-ui.min.js"></script>\r\n    \r\n</head>\r\n\r\n<body>\r\n    <header>test</header>\r\n    <nav class="navbar navbar-default navbar-fixed-top">\r\n        <div class="container" >\r\n            <div class="navbar-header">\r\n                <a class="navbar-brand" href="/">ZouZou</a>\r\n            </div>\r\n            <div id="navbar" class="collapse navbar-collapse">\r\n                <ul class="nav navbar-nav">\r\n                    <li class="active"><a href="/">\u9996\u9875</a></li>\r\n                    <li><a href="#">\u6211\u7684\u5e16\u5b50</a></li>\r\n                    <li><a href="#">\u6211\u7684\u6536\u85cf</a></li>\r\n                </ul>\r\n                <form class="navbar-form form-search navbar-left">  \r\n                    <div class="input-append">  \r\n                        <input type="text" class="form-control white">  \r\n                        <button type="submit" class="btn">\u641c\u7d22</button>  \r\n                    </div>\r\n                </form>\r\n                <ul class="nav navbar-nav navbar-right">\r\n                    <li><a href="#">mingzi</a></li>\r\n                    <li><a href="#">\u6ce8\u9500</a></li>\r\n                </ul>\r\n            </div>\r\n        </div>\r\n    </nav>\r\n    <main></main>\r\n    <footer></footer>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "/base/base.html", "filename": "D:\\Projects\\simple_forum\\templates/base/base.html"}
__M_END_METADATA
"""
