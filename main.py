#!/usr/bin/env python
# -- coding: utf-8 --


# from app.app import app
from app import app
from sys import argv

port = 8000
debug = True

if len(argv) > 1 and argv[1]:
    port = argv[1]

if len(argv) > 2 and argv[2]:
    if argv[2] != 'true':
        debug = False
    pass

if __name__ == '__main__':
    __import__('routers')
    app.run(host = '0.0.0.0', port = int(port), debug = debug)
