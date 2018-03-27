# -- coding: utf-8 --

import os
from index import app   # 导入 app
from flask import render_template, Response

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html', data = {
        "welcome": " hi, this is svon's interface center !! ",
    })


_favicon = None
@app.route('/favicon.ico', methods=['GET'])
def favicon():
    global _favicon #使用全局变量 _favicon
    if not _favicon:
        file = open('%s/static/favicon.ico' % os.path.split(os.path.realpath(__file__))[0], 'rb')
        _favicon = file.read()
    
    return Response(_favicon, content_type='image/x-icon')
