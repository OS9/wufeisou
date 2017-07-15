#!/ubr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 1

if __name__ == '__main__':
    app.run()
