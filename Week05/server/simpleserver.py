#!flask/bin/python

from flask import Flask

# line of code not in lab sheet
# used to define app
# see following for solution:
# https://stackoverflow.com/questions/29277581/flask-nameerror-name-app-is-not-defined

app = Flask(__name__, static_url_path='',static_folder = '../')
# app.config.from_object('config')


@app.route('/')
def index():
    return "<i>Hello, World!</i>"

if __name__ == '__main__' :
    app.run(debug = True)