from flask import Flask
from parserYa import parseyandex

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/start")
def asdfas():
    return "<p>1234123</p>"

@app.route("/yandex")
def yandex():
    return parseyandex()