#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify(status='ok')


if __name__ == '__main__':
    app.run()
