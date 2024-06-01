from flask import Flask, redirect, request
from parserYa import parseyandex

app = Flask(__name__)

@app.route("/")
def hello_world():
    savedData = ''
    with open('fileStorage.txt', 'r') as file:
        while line := file.readline():
            savedData = savedData + line.rstrip()+"<br>"

    page = f'''
    <html>
        <form action="/formProcess" method="POST">
            <input type=text name="myText">
            <input type="submit" value="Сохранить">
        </form>
        <div>
            {savedData}
        </div>
    </html>
    '''
    return page

@app.route("/formProcess", methods=['GET','POST'])
def formProcessing():
    fileStorage = open('fileStorage.txt','a')
    fileStorage.write(request.form['myText']+"\n")
    fileStorage.close()
    return redirect("/", code=302)


@app.route("/start")
def asdfas():
    return "<p>1234123</p>"

@app.route("/yandex")
def yandex():
    return parseyandex()