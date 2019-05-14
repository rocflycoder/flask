#!/usr/bin/env python3
#coding=utf-8

'''请求钩子'''

from flask import Flask,g

app = Flask(__name__)

@app.before_first_request
def foobar_first_request():
    '''在第一次请求时调用，后续不会调用'''
    print("first request")

@app.before_request
def foobar_before_request():
    '''每次请求前处理，包括第一次'''
    print("before request")

@app.after_request
def foobar_after_request(response):
    '''当请求没有异常时，每次请求后调用'''
    print("after request",response)
    return response

@app.teardown_request
def foobar_teardown_request(exception):
    '''有/无异常，每次请求均会调用'''
    print("teardown request",exception)

@app.teardown_appcontext
def teardown_dbz(exception):
    '''应用退出时调用'''
    print('teardown appcontext',exception)

@app.route("/",methods=['GET','POST'])
def hello_world():
    return 'hello world\n'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)