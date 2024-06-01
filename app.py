from flask import Flask, request
from parserYa import parseyandex

app=Flask(__name__)

@app.route("/")
def hello_world():
    page='''
    <html>
        <form action="/formProcess" method="POST">
            <input type=text name="myText">
            <input type="submit" value="Сохранить">
        </form>
    </html>
    '''
    return page

@app.route("/formProcess", methods=['GET','POST'])
def formProcessing():
    return request.form['myText']


@app.route("/start")
def asdfas():
    return "<p>1234123</p>"

@app.route("/yandex")
def yandex():
    return parseyandex()