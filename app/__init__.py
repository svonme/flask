# -- coding: utf-8 --

# 导入 app
from index import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index.html')

def index():
    return render_template('index.html', data = {
        "welcome": " hi, this is svon's interface center !! ",
    })
