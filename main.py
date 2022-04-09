import flask
from flask import Flask, render_template, url_for, request
import requests
import json
import sqlite3
import base64

def decodeb64(coded_st):
    base64.b64decode(coded_st)
    return coded_st

app = Flask(__name__)

@app.route('/try')
def FL():
    f = open('txt.txt')
    f.write(request.args)
    print(request.args)
    return request

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')