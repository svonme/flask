# -- coding: utf-8 --

import os, json
from flask import Flask

app = Flask(__name__)


def set_seting(path = './config.json'):
    src = os.path.abspath(os.path.join('app', path))
    file = open(src, 'rb')
    text = file.read()
    config = json.loads(text)

    labels = ['global', 'mongodb', 'redis', 'mysql', 'secret_key']
    for index in range(len(labels)):
        key = labels[index]
        app.config[key] = config[key]

    pass



set_seting()
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.add_template_global(app.config.get('global'), 'config')
