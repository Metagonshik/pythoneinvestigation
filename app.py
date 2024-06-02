from flask import Flask, redirect, request
from parserYa import parseyandex
from DB_maria import dbExec


app = Flask(__name__)

@app.route("/")
def hello_world():
    savedData = ''
    
    data = dbExec('python_database', 'select * from simpleStrings')
    for i in  range(len(data)):
        savedData = savedData + '<form action="/delete_task" method="POST">' + data[i][1] +  f"""
        <input type='hidden' name='delete_id' value='{data[i][0]}'>
        <input type='submit' value='Удалить'></form><br>"""

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

@app.route("/delete_task", methods=['GET','POST'])
def deleteForm():
    insertSql = f'''DELETE FROM
                        python_database.simpleStrings
	                WHERE id={request.form["delete_id"]};'''

    dbExec('python_database', insertSql)

    return redirect("/", code=302)