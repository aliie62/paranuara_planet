# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:48:19 2019

@author: hosseal
"""

from flask import Flask
from resources.endpoints import get_endpoints
import os

app = Flask(__name__)
app.secret_key = os.environ.get('Flask_Secret_Key')
api = get_endpoints(app)


if __name__ == '__main__':
    app.run(port=5000, debug=True)