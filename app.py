from flask import Flask, redirect, request
from parserYa import parseyandex
from DB_maria import dbExec


app = Flask(__name__)

@app.route("/")
def hello_world():
    savedData = ''
    
    data = dbExec('python_database', 'select * from simpleStrings')
    for i in  range(len(data)):
        savedData = savedData + data[i][1] + "<br>"

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
    insertSql = f'''INSERT INTO
                        python_database.simpleStrings (id, `text`)
                    VALUES
                        (null, "{request.form["myText"]}");'''

    dbExec('python_database', insertSql)

    return redirect("/", code=302)


@app.route("/start")
def asdfas():
    return "<p>1234123</p>"

@app.route("/yandex")
def yandex():
    return parseyandex()