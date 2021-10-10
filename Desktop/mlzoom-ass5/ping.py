# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:16:56 2021

@author: FBI
"""
from flask import Flask

app = Flask('ping')

@app.route('/ping',methods= ['GET'])
def ping():
    return 'pong'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port= 9696)