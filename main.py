#!/usr/bin/env python
# -- coding: utf-8 --


# from app.app import app
from app import app
from sys import argv

@app.route('/')
def hello_world():
    return 'Hello World!'

port = 8000
debug = True

if len(argv) > 1 and argv[1]:
  port = argv[1]

if len(argv) > 2 and argv[2]:
  if argv[2] != 'true':
    debug = False
  pass

# __import__('app.urls')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = int(port), debug = debug)
