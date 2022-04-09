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
    try:
        req = flask.Request.get_data()
        return req
    except:
        return 'Hi'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')